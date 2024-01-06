import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider

VS = 9.6e-4 # Volume du sous-marin ; en m-3, c'est le volume envisagé du sous-marin construit
LAMBDA = 6.3 # Coefficient de frottement... 
ZC = 20 # en m : profondeur cible
g = 9.81
RHO_EAU = 1e3
MASSE_V = 100e-3

TAU = 10 #en secondes, à ajuster après
OFFSET = 8

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

X = np.arange(0, 240, 0.1)

Y = V(X, ZC,TAU)
Y2 = z(X,ZC,TAU)

# --------------------------------------------------------------------Matplotlib : Sorcellerie--------------------------------------------------------------------

ax = plt.axes([0.1, 0.20, 0.4, 0.75])
graphe_V, = ax.plot(X,Y)

ax2 = plt.axes([0.55, 0.2, 0.4, 0.75])
graphe_z, = ax2.plot(X, Y2)


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
curseurTAU = Slider(ax_curseurTAU, r"$\tau$", 0, TAU, valinit=TAU)

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

plt.show()
