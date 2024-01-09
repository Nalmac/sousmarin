class Estimator():
    def __init__(self):
        pass
    
    def calculerT0(self, v_eau, epsilon : float, delta : float) -> float:
        pass
    
    def calculerTau(self, DV : float):
        pass

    def approxVEau(self, v_eau, I : list[float], DV : float):
        from scipy.optimize import minimize_scalar

        f = lambda t : -v_eau(t)
        res = minimize_scalar(f, bounds=I)
        t_max,V_max = res.x,res.fun
        delta_t = V_max/DV
        debut = t_max - delta_t
        fin = t_max + delta_t

        def vApprox(t):
            if t<debut:
                return v_eau(0)
            elif t<= t_max:
                return DV*(t-debut)
            elif t<= fin:
                return V_max - DV*(t-t_max)
            else:
                return v_eau(0)

        return vApprox