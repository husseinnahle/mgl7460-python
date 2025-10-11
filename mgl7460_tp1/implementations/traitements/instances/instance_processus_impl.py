from datetime import datetime
from logging import Logger, getLogger

from mgl7460_tp1.types.modeles.demande_pret import DemandePret
from mgl7460_tp1.types.traitements.definitions.definition_processus import DefinitionProcessus
from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.instances.etat_processus import EtatProcessus
from mgl7460_tp1.types.traitements.instances.etat_traitement import EtatTraitement
from mgl7460_tp1.types.traitements.instances.exception_definition_processus import ExceptionDefinitionProcessus
from mgl7460_tp1.types.traitements.instances.instance_processus import InstanceProcessus
from mgl7460_tp1.types.traitements.instances.instance_tache import InstanceTache
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class InstanceProcessusImpl(InstanceProcessus):

    def __init__(
        self, definition_processus: DefinitionProcessus, demande_pret: DemandePret
    ) -> None:
        self.definition_processus = definition_processus
        self.demande_pret = demande_pret
        self.tache_courante: InstanceTache | None = None
        self.taches: list[InstanceTache] = []
        self.temps_demarrage: datetime | None = None
        self.temps_arret: datetime | None = None
        self.etat_processus: EtatProcessus = EtatProcessus(None, EtatTraitement.PRET)
        self.logger: Logger = getLogger(definition_processus.get_nom())
        self.fabrique = Fabrique.get_singleton_fabrique()

    def get_demande_pret(self) -> DemandePret:
        return self.demande_pret

    def get_definition_processus(self) -> DefinitionProcessus:
        return self.definition_processus

    def get_tache_courante(self) -> InstanceTache | None:
        return self.tache_courante

    def get_taches(self) -> list[InstanceTache]:
        return self.taches

    def get_temps_demarrage(self) -> datetime | None:
        return self.temps_demarrage

    def get_temps_arret(self) -> datetime | None:
        return self.temps_arret

    def get_etat_processus(self) -> EtatProcessus:
        return self.etat_processus

    def get_logger(self) -> Logger:
        return self.logger

    def set_logger(self, logger: Logger) -> None:
        self.logger = logger

    def demarrer(self) -> None:
        self.temps_demarrage = datetime.now()
        definition_tache = self.definition_processus.get_premiere_tache()
        self.tache_courante = self._creer_instance_tache(definition_tache)
        self.etat_processus = EtatProcessus(
            self.tache_courante, EtatTraitement.EN_COURS
        )
        self.tache_courante.executer()
        while self.tache_courante:
            self.etat_processus = EtatProcessus(
                self.tache_courante, EtatTraitement.EN_COURS
            )
            self.tache_courante.executer()
        self.etat_processus = EtatProcessus(None, EtatTraitement.TERMINE)
        self.temps_arret = datetime.now()

    def signaler_fin_tache(self, instance_tache: InstanceTache) -> None:
        self.tache_courante = None
        self.taches.append(instance_tache)
        # Chercher la tache suivante
        definition_tache = instance_tache.get_definition_tache()
        transitions = self.definition_processus.get_transitions_sortantes_de(
            definition_tache
        )
        definition_tache_suivante = []
        for transition in transitions:
            condition = transition.get_condition_transition()
            if condition is None or condition.is_transition_ok(
                instance_tache, self.demande_pret
            ):
                definition_tache_suivante.append(transition.get_tache_destination())
        # Si aucune tache suivante, le processus est terminé
        if len(definition_tache_suivante) == 0:
            return
        # S'il y a plus d'une tache suivante, le processus est mal formé
        elif len(definition_tache_suivante) > 1:
            message = "Plusieurs transitions sortantes trouvées. Votre processus est mal formé."
            raise ExceptionDefinitionProcessus(
                self, [e.get_tache_destination() for e in transitions], message
            )
        # Créer la tache suivante
        tache_suivante = self._creer_instance_tache(definition_tache_suivante[0])
        self.etat_processus = EtatProcessus(tache_suivante, EtatTraitement.PRET)
        self.tache_courante = tache_suivante

    def _creer_instance_tache(
        self, definition_tache: DefinitionTache | None
    ) -> InstanceTache:
        if not definition_tache:
            raise ExceptionDefinitionProcessus(self, [], "Definition de tache absente.")
        instance_tache: InstanceTache = self.fabrique.creer_instance_tache(
            definition_tache, self
        )
        instance_tache.set_demande_pret(self.demande_pret)
        return instance_tache
