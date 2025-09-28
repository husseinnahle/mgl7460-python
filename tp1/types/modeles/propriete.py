from mgl7460.tp1.types.modeles.adresse import Adresse


class Propriete:

    def get_adresse(self) -> Adresse: ...

    def get_valeur_de_marche(self) -> float: ...

    def set_valeur_de_marche(self, valeur: float) -> None: ...
