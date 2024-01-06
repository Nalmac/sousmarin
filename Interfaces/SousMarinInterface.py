from Classes.SousMarin import SousMarin

class SousMarinInterface():
    def __init__(self, submarine : SousMarin):
        self.sous_marin = submarine
    def getMasseVide(self):
        return self.sous_marin.masse_a_vide