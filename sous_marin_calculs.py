import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider

VS = 30e-3 # Volume du sous-marin ; en m-3, c'est le volume envisagé du sous-marin construit
LAMBDA = 80 # Coefficient de frottement... 
ZC = 0.5 # en m : profondeur cible
g = 9.81
RHO_EAU = 1e3
MASSE_V = 29.925

TAU = 5.4 #en secondes, à ajuster après
OFFSET = 5

u = lambda t : t-(OFFSET*TAU)

def z(t,ZC,TAU):
    return ZC/(1+np.exp(-u(t)/TAU))

def dz(t, ZC,TAU):
    return -(1/TAU)*z(t,ZC,TAU)*(1-(z(t,ZC,TAU)/ZC))

def d2z(t, ZC,TAU):
    return (1/TAU**2)*z(t,ZC,TAU)*(1-(z(t,ZC,TAU)/ZC))*(1-(2*z(t,ZC,TAU)/ZC)) 

def rho(t, ZC,TAU):
    return (LAMBDA*dz(t,ZC,TAU)**2 + g*RHO_EAU*VS)/(VS*(g-d2z(t,ZC,TAU)))

def V(t, ZC, TAU): # en L
    return ((VS*rho(t, ZC, TAU) - MASSE_V)/RHO_EAU)*1e3

X = np.arange(0,60, 1)

Y = V(X, ZC,TAU)
Y2 = z(X,ZC,TAU)

# --------------------------------------------------------------------Matplotlib : Sorcellerie--------------------------------------------------------------------

ax = plt.axes([0.1, 0.20, 0.4, 0.75])
graphe_V, = ax.plot(X,Y)
ax.set_xlabel("t")
ax.set_ylabel(r"V(L)")

ax2 = plt.axes([0.55, 0.2, 0.4, 0.75])
graphe_z, = ax2.plot(X, Y2)
ax2.set_xlabel("t")
ax2.set_ylabel("z")


ax_curseurZ = plt.axes([0.25, 0.05, 0.6, 0.03])
curseurZ = Slider(ax_curseurZ, "Profondeur", 0, ZC, valinit=ZC)

def updateZ(event):
    zc = curseurZ.val
    tau = curseurTAU.val
    YPRIME = V(X, zc, tau)
    Y2PRIME = z(X, zc, tau)
    print( f"Nouvelle masse volumique : RHO_MAX = {np.max(YPRIME)}", f" RHO_MIN = {np.min(YPRIME)}")
    graphe_V.set_data(X, YPRIME)
    graphe_z.set_data(X, Y2PRIME)
    plt.draw()

curseurZ.on_changed(updateZ)

ax_curseurTAU = plt.axes([0.25, 0.01, 0.6, 0.03])
curseurTAU = Slider(ax_curseurTAU, r"$\tau$", 0, TAU+1, valinit=TAU)

def updateTAU(event):
    zc = curseurZ.val
    tau = curseurTAU.val
    YPRIME = V(X, zc, tau)
    Y2PRIME = z(X, zc, tau)
    graphe_V.set_data(X, YPRIME)
    graphe_z.set_data(X, Y2PRIME)
    print( f"Nouvelle masse volumique : RHO_MAX = {np.max(YPRIME)}", f" RHO_MIN = {np.min(YPRIME)}")
    plt.draw()

curseurTAU.on_changed(updateTAU)

from scipy import optimize
from scipy.integrate import solve_ivp

result = optimize.minimize_scalar(lambda t : -V(t, ZC, TAU))
result2 = optimize.minimize_scalar(lambda t : V(t, ZC, TAU))
print(result)

plt.show()

# ------------------------------------- Calculer le profil de z obtenu avec une approximation affine de V_eau --------------------------------------

DV = 3.7e-7 # L.s-1
T1 = result.x
Vmax = -result.fun
Veq = 75e-6

dt = (Vmax-Veq)/2 #s
T0 = T1-dt
T2 = T1+dt


print(DV)

def Vaff(t):
    if t<T0:
        return Veq
    elif T0<=t< T1:
        return DV*(t-T0) + Veq
    elif t<T2:
        return DV*(T1-T0) + Veq - DV*(t-T1)
    else:
        return Veq

rhoaff = lambda t : (RHO_EAU*Vaff(t)*1e-3 + MASSE_V)/VS

def equation(t,y):
    if y[0]<0:
        return [y[1],g-(LAMBDA*y[1]**2)/(VS*rhoaff(t))]
    else:
        return [y[1], g*(1-(RHO_EAU/rhoaff(t)))- (LAMBDA*y[1]**2)/(VS*rhoaff(t))]

sol = solve_ivp(equation, [0, 1000], [0, 0])

print(sol)

plt.subplot(121)
plt.plot(sol.t, [Vaff(t) for t in sol.t])
plt.subplot(122)
plt.plot(sol.t,sol.y[0])
plt.show()