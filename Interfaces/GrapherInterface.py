class GrapherInterface():

    from Classes.Grapher import Grapher
    from Interfaces.SolverInterface import SolverInterface
    import numpy as np

    def __init__(self, grapher : Grapher):
        self.grapher = grapher
    def simulation(self, I : np.ndarray, solver : SolverInterface, zc_max : float, tau : float):
        return ()