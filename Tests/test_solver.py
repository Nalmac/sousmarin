import unittest
from Classes.Solver import Solver

class TestSolverCalculations(unittest.TestCase):

    # Solver(SousMarinInterface)
    def setUp(self):
        class FausseInterfaceSousMarin():
            def __init__(self):
                self.masse_a_vide = 500e-3
                self.LAMBDA = 6.3
                self.volume = 1.5e-4
            def getMasseVide(self):
                return self.masse_a_vide
            def get_lambda(self):
                return self.LAMBDA
            def get_volume(self):
                return self.volume
        self.solver = Solver(FausseInterfaceSousMarin())
        self.ZC_TESTS = [2, 5, 7, 10]
        self.TAU_TESTS = [2, 2, 2, 2]

    def testProfondeur(self):
        for i in range(len(self.ZC_TESTS)):
            with self.subTest(i=i):
                z,_ = self.solver.genererZV(self.ZC_TESTS[i], self.TAU_TESTS[i],10)
                self.assertAlmostEqual(z(50),self.ZC_TESTS[i],3)
    
    def testVitesse(self):
        for i in range(len(self.ZC_TESTS)):
            with self.subTest(i=i):
                z,_ = self.solver.genererZV(self.ZC_TESTS[i], self.TAU_TESTS[i],10)
                self.assertAlmostEqual((z(0.01)-z(0))/0.01,0, 1)
    
    def testVolume(self):
        for i in range(len(self.ZC_TESTS)):
            with self.subTest(i=i):
                _,v = self.solver.genererZV(self.ZC_TESTS[i], self.TAU_TESTS[i],10)
                self.assertAlmostEqual(v(0),v(50),3)

if __name__ == '__main__':
    unittest.main()