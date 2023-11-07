import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider

VS = 4 # Volume du sous-marin ; en m-3
LAMBDA = 15 # Coefficient de frottement... 
ZC = 5 # en m : profondeur cible
g = 9.81
RHO_EAU = 1e3

TAU = 2 #en secondes, à ajuster après

u = lambda t : t-(20*TAU)

def z(t,ZC,TAU):
    return ZC/(1+np.exp(-u(t)/TAU))

def dz(t, ZC,TAU):
    return -(1/TAU)*z(t,ZC,TAU)*(1-(z(t,ZC,TAU)/ZC))

def d2z(t, ZC,TAU):
    return (1/TAU**2)*z(t,ZC,TAU)*(1-(z(t,ZC,TAU)/ZC))*(1-(2*z(t,ZC,TAU)/ZC)) 

def rho(t, ZC,TAU):
    return (LAMBDA*dz(t,ZC,TAU)**2 + g*RHO_EAU*VS)/(VS*(g-d2z(t,ZC,TAU)))

X = np.arange(0, 100, 0.1)

Y = rho(X, ZC,TAU)
Y2 = z(X,ZC,TAU)

# Matplotlib : Sorcellerie

ax = plt.axes([0.1, 0.15, 0.8, 0.8])
graphe_rho, = ax.plot(X,Y)

ax_curseurZ = plt.axes([0.25, 0.05, 0.6, 0.03])
curseurZ = Slider(ax_curseurZ, "Profondeur", 0, 100, valinit=5)

def updateZ(event):
    zc = curseurZ.val
    tau = curseurTAU.val
    YPRIME = rho(X, zc, tau)
    graphe_rho.set_data(X, YPRIME)
    plt.draw()

curseurZ.on_changed(updateZ)

ax_curseurTAU = plt.axes([0.25, 0.01, 0.6, 0.03])
curseurTAU = Slider(ax_curseurTAU, r"$\tau$", 0, 100, valinit=2)

def updateTAU(event):
    zc = curseurZ.val
    tau = curseurTAU.val
    YPRIME = rho(X, zc, tau)
    graphe_rho.set_data(X, YPRIME)
    plt.draw()

curseurTAU.on_changed(updateTAU)

plt.show()
