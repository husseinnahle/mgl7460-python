from mgl7460_tp1.types.modeles.adresse import Adresse
from mgl7460_tp1.types.modeles.demande_pret import DemandePret
from mgl7460_tp1.types.modeles.province_ou_territoire import ProvinceOuTerritoire
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class CreationDemandesPret:

    fabrique = Fabrique.get_singleton_fabrique()

    @classmethod
    def get_demande_pret_oui_oui_oui(cls) -> DemandePret:
        demandeur = cls.fabrique.creer_demandeur_pret("Jeanne", "Bergeron", "123-456-789", 120000, 40000, 765)
        propriete = cls.fabrique.creer_propriete(
            Adresse("201A", "2100", "Saint-Urbain", "Montréal", ProvinceOuTerritoire.QUEBEC, "H2X2XH"), 400000
        )
        return cls.fabrique.creer_demande_pret(propriete, demandeur, 405000, 30000)

    @classmethod
    def get_demande_pret_oui_oui_non(cls) -> DemandePret:
        demandeur = cls.fabrique.creer_demandeur_pret("Mamadou", "Diallo", "321-654-987", 120000, 40000, 765)
        propriete = cls.fabrique.creer_propriete(
            Adresse("1504", "1800", "Bleury", "Montréal", ProvinceOuTerritoire.QUEBEC, "H2Y2Y5"), 400000
        )
        return cls.fabrique.creer_demande_pret(propriete, demandeur, 405000, 5000)

    @classmethod
    def get_demande_pret_oui_non_non(cls) -> DemandePret:
        demandeur = cls.fabrique.creer_demandeur_pret("Jorge", "Riviera", "987-654-123", 150000, 50000, 780)
        propriete = cls.fabrique.creer_propriete(
            Adresse("1504", "1800", "Bleury", "Calgary", ProvinceOuTerritoire.ALBERTA, "J3H3G5"), 400000
        )
        return cls.fabrique.creer_demande_pret(propriete, demandeur, 405000, 5000)

    @classmethod
    def get_demande_pret_non_non_non(cls) -> DemandePret:
        demandeur = cls.fabrique.creer_demandeur_pret("Donald", "Trump", "666-666-666", 600000, 83000000, 520)
        propriete = cls.fabrique.creer_propriete(
            Adresse("", "325", "Bay Street", "Toronto", ProvinceOuTerritoire.ONTARIO, "M5H 4G3"), 100000
        )
        return cls.fabrique.creer_demande_pret(propriete, demandeur, 45000000, 5000)

    @classmethod
    def get_demande_pret_oui_non_oui(cls) -> DemandePret:
        demandeur = cls.fabrique.creer_demandeur_pret("François", "Legault", "555-555-555", 275000, 75000, 765)
        propriete = cls.fabrique.creer_propriete(
            Adresse("", "20", "Alströmergatan", "Stockholm", ProvinceOuTerritoire.NEWFOUNDLAND_AND_LABRADOR, "M5H 4G3"),
            480000000,
        )
        return cls.fabrique.creer_demande_pret(propriete, demandeur, 450000000, 275000000)
