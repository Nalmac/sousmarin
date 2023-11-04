from ballast import Ballast, ballast_eq
from scipy.optimize import least_squares
from scipy.integrate import solve_ivp
from constants import *

class SousMarin():
    def __init__(self, ballasts : list[Ballast], m_vide, volume):
        self.ballast = ballast_eq(ballasts)
        self.m_vide = m_vide
        self.masse = m_vide + self.ballast.V*RHO_EAU 
        self.position = (0,0,0) #x,y,z BOND ; avec z vers le bas
        self.volume = volume
        self.coef_f = 10 #????
        self.rho_v = self.m_vide/self.volume
        self.V_eq = (self.volume*RHO_EAU - self.m_vide) / RHO_EAU
    def plongee(self, z):
        def cout(T,S): # Signatures : T = (tau,tf) ; S = (sub,z)
            rho = lambda t : rho_s_d(t, T[0] ,S[1])
            def equation(t,y):
                pass                



def rho_s_d(t, tau, sub : SousMarin):
    if t<tau:
        return rho_s_remplissage(t,sub)
    else:
        return rho_s_vidange(t-tau,sub)

def rho_s_remplissage(t,sub : SousMarin):
    volume_candidat = sub.ballast.Dv*t + sub.ballast.V
    if candidat <= sub.ballast.Vmax:
        sub.ballast.V = volume_candidat
        return (RHO_EAU/sub.volume)*volume_candidat + sub.rho_v
    else:
        sub.ballast.V = sub.ballast.Vmax
        return sub.ballast.V*(RHO_EAU/sub.volume) + sub.rho_v

def rho_s_vidange(t,sub : SousMarin):
    volume_candidat = -sub.ballast.Dv*t + sub.ballast.V
    if candidat >= 0:
        sub.ballast.V = volume_candidat
        return (RHO_EAU/sub.volume)*volume_candidat + sub.rho_v
    else:
        sub.ballast.V = s0
        return sub.rho_v