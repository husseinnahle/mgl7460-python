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


class Fabrique:

    _instance = None

    @classmethod
    def creer_propriete(cls, adresse: Adresse, valeur_de_marche: float | None = None) -> Propriete: ...

    @classmethod
    def creer_demandeur_pret(
        cls,
        prenom: str,
        nom: str,
        NAS: str,
        revenu_annel: float | None = None,
        obligations_anuelles: float | None = None,
        score_credit: float | None = None,
    ) -> DemandeurPret: ...

    @classmethod
    def creer_demande_pret(
        cls,
        propriete: Propriete,
        demandeur_pret: DemandeurPret,
        prix_achat: float | None = None,
        mise_de_fonds: float | None = None,
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
    def creer_definition_processus(cls, nom_processus: str, description_processus: str) -> DefinitionProcessus: ...

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
        from mgl7460_tp1.implementations.utils.fabrique import FabriqueImpl
        if Fabrique._instance is None:
            Fabrique._instance = FabriqueImpl()
        return Fabrique._instance
