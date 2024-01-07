class Solver():

    from Utils.Constants import *
    from Interfaces.SousMarinInterface import SousMarinInterface

    def __init__(self, sous_marin : SousMarinInterface):
        self.sous_marin = sous_marin
    def solveRho(self,dz,d2z):
        LAMBDA = self.sous_marin.get_lambda()
        volume = self.sous_marin.get_volume()

        return (lambda t : (LAMBDA*(dz(t)**2) + g*RHO_EAU*volume)/(volume*(g-d2z(t))) )

    def vEauFromRho(self, rho):
        vs = self.sous_marin.get_volume()
        masse_a_vide = self.sous_marin.getMasseVide()
        return (lambda t : (vs*rho(t) - masse_a_vide)/(RHO_EAU))

    def genererZV(self, zc : float, tau : float, phi : float):
        from Utils.Sigmoide import genererOrdre2
        z,dz,d2z = genererOrdre2(zc, tau, phi)
        