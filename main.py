from Classes.Ballast import Ballast
from Classes.SousMarin import SousMarin
from Classes.Solver import Solver
from Classes.Grapher import Grapher
from Interfaces.BallastInterface import BallastInterface
from Interfaces.SolverInterface import SolverInterface
from Interfaces.SousMarinInterface import SousMarinInterface

ballast = Ballast(1, 20, 0)
interface_ballast = BallastInterface(ballast)

sub = SousMarin(interface_ballast, LAMBDA=6.3, masse_a_vide=0.72, volume=0.8e-3)
interface_sub = SousMarinInterface(submarine=sub)

ordi = Solver(sous_marin=interface_sub)
interface_ordi = SolverInterface(ordi)

logiciel_graph = Grapher()

logiciel_graph.simulation([0, 200], solver=ordi, zc_max=15, tau=10, phi=100)