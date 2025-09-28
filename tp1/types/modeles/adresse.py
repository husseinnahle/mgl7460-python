class Adresse:
    def __init__(
        self,
        numero_porte: str,
        numero_rue: str,
        nom_rue: str,
        nom_ville: str,
        province,
        code_postal: str,
    ):
        self.numero_porte = numero_porte
        self.numero_rue = numero_rue
        self.nom_rue = nom_rue
        self.nom_ville = nom_ville
        self.province = province
        self.code_postal = code_postal

    def __str__(self):
        return f"Porte {self.numero_porte}, {self.numero_rue} rue {self.nom_rue}, {self.nom_ville}, {self.code_postal} {self.province}"
