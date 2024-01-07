class SousMarinInterface():

    from Classes.SousMarin import SousMarin
    
    def __init__(self, submarine : SousMarin):
        self.sous_marin = submarine
    def getMasseVide(self):
        return self.sous_marin.masse_a_vide
    def get_lambda(self):
        return self.sous_marin.LAMBDA
    def get_volume(self):
        return self.sous_marin.volume