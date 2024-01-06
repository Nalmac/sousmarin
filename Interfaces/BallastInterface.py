from Classes.Ballast import Ballast

class BallastInterface():
    def __init__(self, ballast : Ballast):
        self.ballast = ballast
    def getDv(self):
        return self.ballast.dv
    def getVeau(self):
        return self.ballast.v_eau