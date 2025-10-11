from mgl7460_tp1.types.modeles.demandeur_pret import DemandeurPret


class DemandeurPretImpl(DemandeurPret):

    def __init__(
        self,
        nom: str,
        prenom: str,
        nas: str,
        revenu_annuel: float,
        obligations_annuelles: float,
        score_credit: int,
    ) -> None:
        self.nom = nom
        self.prenom = prenom
        self.nas = nas
        self.revenu_annuel = revenu_annuel
        self.obligations_annuelles = obligations_annuelles
        self.score_credit = score_credit

    def get_nom(self) -> str:
        return self.nom

    def get_prenom(self) -> str:
        return self.prenom

    def get_nas(self) -> str:
        return self.nas

    def get_revenu_annuel(self) -> float:
        return self.revenu_annuel

    def set_revenu_annuel(self, revenu: float) -> None:
        self.revenu_annuel = revenu

    def get_obligations_annuelles(self) -> float:
        return self.obligations_annuelles

    def set_obligations_annuelles(self, obligations: float) -> None:
        self.obligations_annuelles = obligations

    def get_taux_endettement(self) -> float:
        if self.revenu_annuel == 0:
            return 0
        return self.obligations_annuelles / self.revenu_annuel

    def get_score_credit(self) -> int:
        return self.score_credit

    def set_score_credit(self, score: int) -> None:
        self.score_credit = score
