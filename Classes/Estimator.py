class Estimator():
    def __init__(self):
        pass
    
    from Utils.FunctionsUtils import calculerMax

    #OK
    def calculerT0(self, v_eau, epsilon : float, delta : float) -> float:
        n = 0
        while abs(v_eau(n*delta) - v_eau((n+1)*delta)) <= epsilon:
            n+=1
        return n*delta

    from Interfaces.SolverInterface import SolverInterface
    
    def calculerPente(self, ZC : float, tau : float, phi : float, I : list[float], epsilon : float, delta : float, solver : SolverInterface):
        from Utils.FunctionsUtils import calculerMax
        _,v = solver.genererZV(ZC, tau, phi)
        t0 = self.calculerT0(v_eau=v, epsilon=epsilon, delta=delta)
        t_max,V_max = calculerMax(v=v, I=I)
        pente = (V_max-v(t0))/(t_max-t0)

        return pente
  
    
    
    def calculerTau(self, DV : float, ZC : float, epsilon : float, phi : float, I : list[float], solver : SolverInterface, tauMax : float = 20):
        pas = 0.01
        tau = 1
        pente = self.calculerPente(ZC, tau, phi, I, pas, pas, solver)
        while abs(pente - DV) > epsilon and tau <= tauMax:
            tau += pas
            pente = self.calculerPente(ZC, tau, phi, I, pas, pas, solver)

        if tau <= tauMax:
            print(tau)
            return tau
        else:
            raise ValueError(tauMax) 
        

    def approxVEau(self, v_eau, I : list[float], DV : float):
        from Utils.FunctionsUtils import calculerMax
        t_max,V_max = calculerMax(v_eau,I)
        delta_t = V_max/DV
        debut = t_max - delta_t
        fin = t_max + delta_t

        def vApprox(t):
            if t<debut:
                return v_eau(0)
            elif t<= t_max:
                return DV*(t-debut) + v_eau(0)
            elif t<= fin:
                return V_max - DV*(t-t_max)
            else:
                return v_eau(0)

        return vApprox
    
    def genererVEauAffine(self, DV : float, ZC : float, epsilon : float, phi : float, I : list[float], solver : SolverInterface):
        tau = self.calculerTau(DV, ZC, epsilon, phi, I, solver)
        _,v_eau = solver.genererZV(ZC, tau, phi)

        return self.approxVEau(v_eau, I, DV)