class Estimator():
    def __init__(self):
        pass

    def approxVEau(v_eau, I : list[float], DV : float):
        from scipy.optimize import minimize_scalar

        f = lambda t : -v_eau(t)
        res = minimize_scalar(f, bounds=I)
        t_max,V_max = res.x,res.fun
        delta_t = V_max/DV
        debut = t_max - delta_t
        fin = t_max + delta_t

        def vApprox(t):
            if t<debut:
                return 0
            elif t<= t_max:
                return DV*(t-debut)
            elif t<= fin:
                return V_max - DV*(t-t_max)
            else:
                return 0

        return vApprox