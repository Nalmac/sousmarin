import numpy as np

class Ballast():
    def __init__(self, Vmax, Dv):
        self.Vmax = Vmax
        self.Dv = Dv
        self.V = 0 #Initialement, le ballast est vide d'eau
    def remplir(self, T, dt): #I intervalle de temps
        I = np.arange(0, T, dt)
        for t in I:
            if self.V + self.Dv*dt <= self.Vmax:
                self.V += self.Dv*dt
        return self.V
        
