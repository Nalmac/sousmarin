from Interfaces.BallastInterface import BallastInterface

class SousMarin():
    def __init__(self, interface_ballast : BallastInterface, LAMBDA, masse_a_vide, volume):
        self.ballast = interface_ballast
        self.volume = volume
        self.LAMBDA = LAMBDA
        self.masse_a_vide = masse_a_vide