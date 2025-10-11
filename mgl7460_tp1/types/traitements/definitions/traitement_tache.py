from logging import Logger
from typing import Callable

from mgl7460_tp1.types.modeles.demande_pret import DemandePret


class TraitementTache:

    def __init__(self, traitement: Callable[[DemandePret, Logger], bool]):
        self.traitement = traitement

    def traiter_demande_pret(self, demande: DemandePret | None, logger: Logger) -> bool:
        if demande is None:
            raise ValueError("Aucune demande de prêt fournie pour le traitement.")
        return self.traitement(demande, logger)
