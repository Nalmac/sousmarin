import numpy as np

class Ballast():
    def __init__(self, Vmax, Dv, V=0):
        self.Vmax = Vmax
        self.Dv = Dv
        self.V = V #Initialement, le ballast est vide d'eau, par défaut
    def remplir(self, T, dt): #I intervalle de temps
        I = np.arange(0, T, dt)
        for t in I:
            if self.V + self.Dv*dt <= self.Vmax:
                self.V += self.Dv*dt
        return self.V

def ballast_eq(ballasts: list[Ballast]):
    # On suppose que les débits volumiques sont les mêmes
    Vmax = 0
    for b in ballasts:
        Vmax += b.Vmax
    return Ballast(Vmax, ballasts[0].Dv)
