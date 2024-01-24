def calculerMax(v, I):
        from scipy.optimize import minimize_scalar

        f = lambda t : -v(t)
        res = minimize_scalar(f, bounds=I)
        t_max,V_max = res.x,res.fun
        return t_max, -V_max