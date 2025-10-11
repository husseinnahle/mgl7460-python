from datetime import datetime

from mgl7460_tp1.types.modeles.demande_pret import DemandePret
from mgl7460_tp1.types.modeles.demandeur_pret import DemandeurPret
from mgl7460_tp1.types.modeles.propriete import Propriete
from mgl7460_tp1.types.modeles.resultat import Resultat
from mgl7460_tp1.types.modeles.resultat_traitement import ResultatTraitement
from mgl7460_tp1.types.modeles.termes_pret import TermesPret
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class DemandePretImpl(DemandePret):

    def __init__(
        self,
        propriete: Propriete,
        demandeur_pret: DemandeurPret,
        prix_achat: float,
        mise_de_fonds: float,
        numero_demande: str | None = None,
        termes_pret: TermesPret | None = None,
    ) -> None:
        self.numero_demande = numero_demande
        self.date_demande = datetime.now()
        self.demandeur_pret = demandeur_pret
        self.propriete = propriete
        self.mise_de_fonds = mise_de_fonds
        self.prix_achat = prix_achat
        self.termes_pret = termes_pret
        self.resultat_traitement = (
            Fabrique.get_singleton_fabrique().creer_resultat_traitement(
                Resultat.ACCEPTEE
            )
        )

    def get_numero_demande(self) -> str | None:
        return self.numero_demande

    def get_date_demande(self) -> datetime:
        return self.date_demande

    def get_demandeur_pret(self) -> DemandeurPret:
        return self.demandeur_pret

    def get_propriete(self) -> Propriete:
        return self.propriete

    def get_montant_pret(self) -> float:
        return self.prix_achat - self.mise_de_fonds

    def get_montant_mise_de_fonds(self) -> float:
        return self.mise_de_fonds

    def set_montant_mise_de_fonds(self, montant: float) -> None:
        self.mise_de_fonds = montant

    def get_resultat_traitement(self) -> ResultatTraitement:
        return self.resultat_traitement

    def set_resultat_traitement(self, resultat_traitement: ResultatTraitement) -> None:
        if resultat_traitement.get_resultat() == Resultat.REFUSEE:
            self.resultat_traitement.set_resultat(Resultat.REFUSEE)
            for message in resultat_traitement.get_messages():
                self.resultat_traitement.ajouter_message(message)

    def get_ratio_emprunt_valeur(self) -> float:
        return self.get_montant_pret() / self.propriete.get_valeur_de_marche()

    def get_prix_achat(self) -> float:
        return self.prix_achat

    def set_prix_achat(self, prix: float) -> None:
        self.prix_achat = prix

    def get_termes_pret(self) -> TermesPret | None:
        return self.termes_pret

    def set_termes_pret(self, termes: TermesPret) -> None:
        self.termes_pret = termes
