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

    def creer_propriete(self, adresse: Adresse, valeur_marche: float | None = None) -> Propriete: ...

    def creer_demandeur_pret(
        self,
        prenom: str,
        nom: str,
        NAS: str,
        revenu_annel: float | None = None,
        obligations_anuelles: float | None = None,
        score_credit: float | None = None,
    ) -> DemandeurPret: ...

    def creer_demande_pret(
        self,
        propriete: Propriete,
        demandeur_pret: DemandeurPret,
        prix_achat: float | None = None,
        mise_de_fonds: float | None = None,
    ) -> DemandePret: ...

    def creer_resultat_traitement(self, resultat: Resultat) -> ResultatTraitement: ...

    def creer_definition_tache(
        self, nom: str, description: str, traitement_tache: TraitementTache | None
    ) -> DefinitionTache: ...

    def creer_definition_transition(
        self,
        tache_source: DefinitionTache,
        tache_destination: DefinitionTache,
        condition_transition: ConditionTransition | None = None,
    ) -> DefinitionTransition: ...

    def creer_definition_processus(self, nom_processus: str, description_processus: str) -> DefinitionProcessus: ...

    def creer_instance_processus(
        self, definition_processus: DefinitionProcessus, demande_pret: DemandePret
    ) -> InstanceProcessus: ...

    def creer_instance_tache(
        self, definition_tache: DefinitionTache, instance_processus: InstanceProcessus
    ) -> InstanceTache: ...

    @staticmethod
    def get_singleton_fabrique() -> "Fabrique": ...
