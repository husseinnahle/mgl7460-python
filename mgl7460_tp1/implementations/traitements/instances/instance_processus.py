from datetime import datetime
from logging import Logger

from mgl7460_tp1.types.modeles.demande_pret import DemandePret
from mgl7460_tp1.types.traitements.definitions.definition_processus import DefinitionProcessus
from mgl7460_tp1.types.traitements.instances.etat_processus import EtatProcessus
from mgl7460_tp1.types.traitements.instances.etat_traitement import EtatTraitement
from mgl7460_tp1.types.traitements.instances.instance_processus import InstanceProcessus
from mgl7460_tp1.types.traitements.instances.instance_tache import InstanceTache
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class InstanceProcessusImpl(InstanceProcessus):

    def __init__(self, definition_processus: DefinitionProcessus, demande_pret: DemandePret) -> None:
        self.definition_processus = definition_processus
        self.demande_pret = demande_pret
        self.tache_courante: InstanceTache | None = None
        self.taches: list[InstanceTache] = []
        self.temps_demarrage: datetime | None = None
        self.temps_arret: datetime | None = None
        self.etat_processus: EtatProcessus | None = None
        self.logger: Logger | None = None

    def get_demande_pret(self) -> DemandePret:
        return self.demande_pret

    def get_definition_processus(self) -> DefinitionProcessus:
        return self.definition_processus

    def get_tache_courante(self) -> InstanceTache:
        return self.tache_courante

    def get_taches(self) -> list[InstanceTache]:
        return self.taches

    def get_temps_demarrage(self) -> datetime:
        return self.temps_demarrage

    def get_temps_arret(self) -> datetime:
        return self.temps_arret

    def get_etat_processus(self) -> EtatProcessus:
        if self.tache_courante is None:
            return EtatProcessus(None, EtatTraitement.PRET)
        else:
            return EtatProcessus(self.tache_courante, EtatTraitement.EN_COURS)

    def get_logger(self) -> Logger:
        return self.logger

    def set_logger(self, logger: Logger) -> None:
        self.logger = logger

    def demarrer(self) -> None:

        self.temps_demarrage = datetime.now()

        definition_tache_courante = self.definition_processus.get_premiere_tache()
        instance_tache_courante: InstanceTache = Fabrique.creer_instance_tache(definition_tache_courante, self)
        instance_tache_courante.executer()

        


        self.temps_arret = datetime.now()


    def signaler_fin_tache(self, instance_tache: InstanceTache) -> None: ...
