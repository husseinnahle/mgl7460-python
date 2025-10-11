from mgl7460_tp1.types.modeles.adresse import Adresse
from mgl7460_tp1.types.modeles.propriete import Propriete


class ProprieteImpl(Propriete):

    def __init__(self, adresse: Adresse, valeur_de_marche: float) -> None:
        self.adresse = adresse
        self.valeur_de_marche = valeur_de_marche

    def get_adresse(self) -> Adresse:
        return self.adresse

    def get_valeur_de_marche(self) -> float:
        return self.valeur_de_marche

    def set_valeur_de_marche(self, valeur: float) -> None:
        self.valeur_de_marche = valeur
