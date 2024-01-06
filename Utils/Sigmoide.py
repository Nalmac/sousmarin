from numpy import exp

def genererOrdre2(A,tau,phi):
    u = lambda t : t-(phi*tau)

    def z(t):
        return A/(1+np.exp(-u(t)/tau))

    def dz(t):
        return -(1/tau)*z(t)*(1-(z(t)/A))

    def d2z(t):
        return (1/tau**2)*z(t)*(1-(z(t)/A))*(1-(2*z(t)/A))
    
    return z,dz,d2z