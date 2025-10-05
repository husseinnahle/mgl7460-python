from datetime import datetime
from logging import Logger

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

    def __init__(self, definition_processus: DefinitionProcessus, demande_pret: DemandePret) -> None:
        self.definition_processus = definition_processus
        self.demande_pret = demande_pret
        self.tache_courante: InstanceTache | None = None
        self.taches: list[InstanceTache] = []
        self.temps_demarrage: datetime | None = None
        self.temps_arret: datetime | None = None
        self.etat_processus: EtatProcessus | None = None
        self.logger: Logger | None = None
        self.fabrique = Fabrique.get_singleton_fabrique()

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
        return self.etat_processus

    def get_logger(self) -> Logger:
        return self.logger

    def set_logger(self, logger: Logger) -> None:
        self.logger = logger

    def demarrer(self) -> None:
        self.temps_demarrage = datetime.now()
        definition_tache = self.definition_processus.get_premiere_tache()
        self.tache_courante = self._creer_instance_tache(definition_tache)
        self.etat_processus = EtatProcessus(self.tache_courante, EtatTraitement.PRET)
        self.tache_courante.executer()
        while self.tache_courante is not None:
            self.tache_courante.executer()
        self.etat_processus = EtatProcessus(self.tache_courante, EtatTraitement.TERMINE)
        self.temps_arret = datetime.now()

    def signaler_fin_tache(self, instance_tache: InstanceTache) -> None:
        # Enregistrer la tâche terminée
        self.taches.append(instance_tache)
        # Chercher la prochaine tâche à exécuter
        definition_tache = instance_tache.get_definition_tache()
        transitions = self.definition_processus.get_transitions_sortantes_de(definition_tache)
        # Aucun transition sortante : fin du processus
        if len(transitions) == 0:
            return
        # Plusieurs transitions sortantes : erreur de définition du processus
        elif len(transitions) > 1:
            message = "Plusieurs transitions sortantes trouvées. Votre processus est mal formé."
            raise ExceptionDefinitionProcessus(self, [e.get_tache_destination() for e in transitions], message)
        # Une seule transition sortante : continuer le processus
        transition = transitions[0]
        condition = transition.get_condition_transition()
        # Vérifier si la condition de transition est satisfaite
        if not condition.is_transition_ok(definition_tache, self.demande_pret):
            return
        # Créer et configurer la tâche suivante
        definition_tache_suivante = transition.get_tache_destination()
        tache_suivante: InstanceTache = self.fabrique.creer_instance_tache(definition_tache_suivante, self)
        self.etat_processus = EtatProcessus(tache_suivante, EtatTraitement.PRET)

    def _creer_instance_tache(self, definition_tache: DefinitionTache) -> InstanceTache:
        instance_tache: InstanceTache = self.fabrique.creer_instance_tache(definition_tache, self)
        instance_tache.set_demande_pret(self.demande_pret)
        return instance_tache
