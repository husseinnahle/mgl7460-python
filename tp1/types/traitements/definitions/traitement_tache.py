from logging import Logger

from mgl7460.tp1.types.modeles.demande_pret import DemandePret


class TraitementTache:

    def traiter_demande_pret(self, demande_pret: DemandePret, logger: Logger) -> bool: ...
