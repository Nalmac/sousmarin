import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp
from Utils.Constants import *

DV = 0.37e-3 # L.s-1
Vmax = 0.082
Veq = 75e-3
T1 = (Vmax - Veq)/DV
T2 = 2*T1 + 10
MASSE_V = 29.925
VS = 30e-3
LAMBDA = 80

def V(t):
    if t< T1:
        return DV*t + Veq
    elif t<T2:
        return DV*T1 + Veq - DV*(t-T1)
    else:
        return min(75e-3, Veq - DV*10 + DV*(t-T2))

rhoaff = lambda t : (RHO_EAU*V(t)*1e-3 + MASSE_V)/VS

def equation(t,y):
    if y[0]<0:
        return [y[1],g-(LAMBDA*y[1]**2)/(VS*rhoaff(t))]
    else:
        return [y[1], g*(1-(RHO_EAU/rhoaff(t)))- (LAMBDA*y[1]**2)/(VS*rhoaff(t))]

sol = solve_ivp(equation, [0, 100], [0, 0])

print(sol)

plt.subplot(121)
plt.plot(sol.t, [V(t) for t in sol.t])
plt.subplot(122)
plt.plot(sol.t,sol.y[0])
plt.show()