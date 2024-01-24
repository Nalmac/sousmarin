from Classes.Ballast import Ballast
from Classes.SousMarin import SousMarin
from Classes.Solver import Solver
from Classes.Grapher import Grapher
from Interfaces.BallastInterface import BallastInterface
from Interfaces.SolverInterface import SolverInterface
from Interfaces.SousMarinInterface import SousMarinInterface

from Classes.Estimator import Estimator

ballast = Ballast(1, 20, 0)
interface_ballast = BallastInterface(ballast)

sub = SousMarin(interface_ballast, LAMBDA=6.3, masse_a_vide=0.72, volume=0.8e-3)
interface_sub = SousMarinInterface(submarine=sub)

ordi = Solver(sous_marin=interface_sub)
interface_ordi = SolverInterface(ordi)

logiciel_graph = Grapher()

# Partie de test, pas final

logiciel_estimation = Estimator()

v = logiciel_estimation.genererVEauAffine(5e-6, 3, 0.01, 5, [0,500], interface_ordi)

import matplotlib.pyplot as plt
import numpy as np

X = np.arange(0, 500, 0.1)
Y = [v(t) for t in X]
plt.plot(X,Y)
plt.show()