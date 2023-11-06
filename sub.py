from ballast import Ballast, ballast_eq
from constants import *

from scipy.optimize import least_squares
from scipy.integrate import solve_ivp
import numpy as np

# -------------------------------------------------------------------------- Constantes--------------------------------------------------------------------

VS = 4 # Volume du sous-marin ; en m-3
MASSE_V = 100 # masse à vide du sous-marin en kg
RHO_V = MASSE_V/VS # masse volumique, à vide, du sous-marin
V_EAU_EQ = (VS*RHO_EAU - MASSE_V)/RHO_EAU # Volume d'eau nécessaire pour l'équilibre poids / Archimède
DV = 2e-1 # Débit volumique en m-3.s-1
V_EAU_0 = 0 # Volume d'eau initialement présent dans les ballasts ; en m-3
V_EAU_MAX = 3 # Volume d'eau maximal ie capacité des ballasts en m-3
Z_INITIALE,V_INITIALE = 0,0 # Profondeur et vitesse initiales respectivment en m et m.s-1
LAMBDA = 100 # Coefficient de frottement... 
ZC = 5 # en m : profondeur cible
g = 9.81
RHO_EAU = 1e3

# -------------------------------------------------------- Évolution de la masse volumique durant la descente ----------------------------------------------

def v_eau(t : float, TAU : float) -> float:
    V_TAU = V_EAU_0 + DV*TAU
    if t < TAU:
        return V_EAU_0 + DV*t if V_EAU_0 + DV*t < V_EAU_MAX else V_EAU_MAX
    else:
        return V_TAU - DV*(t-TAU) if V_TAU - DV*(t-TAU) > V_EAU_EQ else V_EAU_EQ

def rho(t : float, TAU : float) -> float:
    return (RHO_EAU*v_eau(t,TAU) + MASSE_V)/VS

# ------------------------------------------------------- Équation du mouvement en fonction de la constante tau --------------------------------------------

def creer_equation(TAU : float):
    rho_s = lambda t : rho(t, TAU)
    m = lambda t : rho_s(t)*VS
    def equation(t,y):
        def archi(z,t):
            if z>0:
                return g*(1 - (RHO_EAU/rho_s(t)))
            else:
                return g
        d2z = archi(y[0],t) - ((LAMBDA*(y[1]**2))/m(t))
        return [y[1], d2z]
    return equation

# --------------------------------------------------------------- Calcul du coût d'une solution donnée ------------------------------------------------------

def cout(z : list[float], vz : list[float] , ZC : float, TAU : float, TF : float) -> float :
    if TAU +1 >= TF:
        return 1e6
    else:
        return np.abs(z[-1]-ZC) + np.abs(vz[-1])

# ------------------------------------------------------- Optimisation d'une fonction pour trouver TAU et TF ------------------------------------------------

def optimiser(T : list[float]) -> float: # T = [TAU, TF]
    eq = creer_equation(T[0])
    solution = solve_ivp(eq, [0,T[1]], [Z_INITIALE,V_INITIALE])
    print(solution.message)
    z,vz = solution.y[0],solution.y[1]
    return cout(z,vz, ZC, T[0], T[1])

# sidieuleveut = least_squares(optimiser, [0.1,5])
# print(sidieuleveut)

print(optimiser([1,5]))

