from Classes.Solver import Solver

class SolverInterface():
    def __init__(self, solver : Solver):
        self.solver = solver
    def solveRho(self, dz,d2z):
        return self.solver.solveRho(dz,d2z)
    def vEauFromRho(self, rho):
        return self.solver.vEauFromRho(rho)