from typing import Protocol

from mgl7460_tp1.types.modeles.adresse import Adresse
from mgl7460_tp1.types.modeles.demande_pret import DemandePret
from mgl7460_tp1.types.modeles.demandeur_pret import DemandeurPret
from mgl7460_tp1.types.modeles.propriete import Propriete
from mgl7460_tp1.types.modeles.resultat import Resultat
from mgl7460_tp1.types.modeles.resultat_traitement import ResultatTraitement
from mgl7460_tp1.types.traitements.definitions.condition_transition import ConditionTransition
from mgl7460_tp1.types.traitements.definitions.definition_processus import DefinitionProcessus
from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.definitions.definition_transition import DefinitionTransition
from mgl7460_tp1.types.traitements.definitions.traitement_tache import TraitementTache
from mgl7460_tp1.types.traitements.instances.instance_processus import InstanceProcessus
from mgl7460_tp1.types.traitements.instances.instance_tache import InstanceTache


class Fabrique(Protocol):

    @classmethod
    def creer_propriete(
        cls, adresse: Adresse, valeur_de_marche: float
    ) -> Propriete: ...

    @classmethod
    def creer_demandeur_pret(
        cls,
        prenom: str,
        nom: str,
        NAS: str,
        revenu_annuel: float,
        obligations_annuelles: float,
        score_credit: int,
    ) -> DemandeurPret: ...

    @classmethod
    def creer_demande_pret(
        cls,
        propriete: Propriete,
        demandeur_pret: DemandeurPret,
        prix_achat: float,
        mise_de_fonds: float,
    ) -> DemandePret: ...

    @classmethod
    def creer_resultat_traitement(cls, resultat: Resultat) -> ResultatTraitement: ...

    @classmethod
    def creer_definition_tache(
        cls, nom: str, description: str, traitement_tache: TraitementTache | None = None
    ) -> DefinitionTache: ...

    @classmethod
    def creer_definition_transition(
        cls,
        tache_source: DefinitionTache,
        tache_destination: DefinitionTache,
        condition_transition: ConditionTransition | None = None,
    ) -> DefinitionTransition: ...

    @classmethod
    def creer_definition_processus(
        cls, nom_processus: str, description_processus: str
    ) -> DefinitionProcessus: ...

    @classmethod
    def creer_instance_processus(
        cls, definition_processus: DefinitionProcessus, demande_pret: DemandePret
    ) -> InstanceProcessus: ...

    @classmethod
    def creer_instance_tache(
        cls, definition_tache: DefinitionTache, instance_processus: InstanceProcessus
    ) -> InstanceTache: ...

    @staticmethod
    def get_singleton_fabrique() -> "Fabrique":
        from mgl7460_tp1.implementations.utils.fabrique_impl import FabriqueImpl

        return FabriqueImpl()
