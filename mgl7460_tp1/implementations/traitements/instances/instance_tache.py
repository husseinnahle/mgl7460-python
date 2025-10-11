from mgl7460_tp1.types.modeles.demande_pret import DemandePret
from mgl7460_tp1.types.modeles.resultat import Resultat
from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.instances.etat_traitement import EtatTraitement
from mgl7460_tp1.types.traitements.instances.instance_processus import InstanceProcessus
from mgl7460_tp1.types.traitements.instances.instance_tache import InstanceTache
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class InstanceTacheImpl(InstanceTache):

    def __init__(
        self,
        definition_tache: DefinitionTache,
        processus_englobant: InstanceProcessus,
    ) -> None:
        self.definition_tache = definition_tache
        self.processus_englobant = processus_englobant
        self.demande_pret: DemandePret | None = None
        self.etat_instance_tache: EtatTraitement = EtatTraitement.NON_DEMARRE

    def get_definition_tache(self) -> DefinitionTache:
        return self.definition_tache

    def get_etat_instance_tache(self) -> EtatTraitement:
        return self.etat_instance_tache

    def set_etat_instance_tache(self, etat_traitement: EtatTraitement) -> None:
        self.etat_instance_tache = etat_traitement

    def get_processus_englobant(self) -> InstanceProcessus:
        return self.processus_englobant

    def get_demande_pret(self) -> DemandePret:
        return self.demande_pret

    def set_demande_pret(self, demande_pret: DemandePret) -> None:
        self.demande_pret = demande_pret

    def executer(self) -> None:
        logger = self.processus_englobant.get_logger()
        tache = self.definition_tache.get_traitement_tache()
        self.etat_instance_tache = EtatTraitement.EN_COURS
        resultat = tache.traiter_demande_pret(self.demande_pret, logger)
        resultat = Resultat.ACCEPTEE if resultat else Resultat.REFUSEE
        fabrique = Fabrique.get_singleton_fabrique()
        resultat_traitement = fabrique.creer_resultat_traitement(resultat)
        if resultat == Resultat.REFUSEE:
            resultat_traitement.ajouter_message(f"La tâche '{self.definition_tache.get_nom()}' a échoué.")
        self.demande_pret.set_resultat_traitement(resultat_traitement)
        self.etat_instance_tache = EtatTraitement.TERMINE
        self.processus_englobant.signaler_fin_tache(self)
