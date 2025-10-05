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
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class FabriqueImpl(Fabrique):

    @classmethod
    def creer_propriete(cls, adresse: Adresse, valeur_de_marche: float | None = None) -> Propriete:
        from mgl7460_tp1.implementations.modeles.propriete import ProprieteImpl
        return ProprieteImpl(adresse=adresse, valeur_de_marche=valeur_de_marche)

    @classmethod
    def creer_demandeur_pret(
        cls,
        prenom: str,
        nom: str,
        nas: str,
        revenu_annuel: float | None = None,
        obligations_annuelles: float | None = None,
        score_credit: float | None = None,
    ) -> DemandeurPret:
        from mgl7460_tp1.implementations.modeles.demandeur_pret import DemandeurPretImpl
        return DemandeurPretImpl(
            prenom=prenom,
            nom=nom,
            nas=nas,
            revenu_annuel=revenu_annuel,
            obligations_annuelles=obligations_annuelles,
            score_credit=score_credit,
        )

    @classmethod
    def creer_demande_pret(
        cls,
        propriete: Propriete,
        demandeur_pret: DemandeurPret,
        prix_achat: float | None = None,
        mise_de_fonds: float | None = None,
    ) -> DemandePret:
        from mgl7460_tp1.implementations.modeles.demande_pret import DemandePretImpl
        return DemandePretImpl(
            propriete=propriete,
            demandeur_pret=demandeur_pret,
            prix_achat=prix_achat,
            mise_de_fonds=mise_de_fonds,
        )

    @classmethod
    def creer_resultat_traitement(cls, resultat: Resultat) -> ResultatTraitement:
        from mgl7460_tp1.implementations.modeles.resultat_traitement import ResultatTraitementImpl
        return ResultatTraitementImpl(resultat=resultat)

    @classmethod
    def creer_definition_tache(
        cls, nom: str, description: str, traitement_tache: TraitementTache | None = None
    ) -> DefinitionTache:
        from mgl7460_tp1.implementations.traitements.definitions.definition_tache import DefinitionTacheImpl
        return DefinitionTacheImpl(nom=nom, description=description, traitement=traitement_tache)

    @classmethod
    def creer_definition_transition(
        cls,
        tache_source: DefinitionTache,
        tache_destination: DefinitionTache,
        condition_transition: ConditionTransition | None = None,
    ) -> DefinitionTransition:
        from mgl7460_tp1.implementations.traitements.definitions.definition_transition import DefinitionTransitionImpl
        return DefinitionTransitionImpl(
            tache_source=tache_source,
            tache_destination=tache_destination,
            condition_transition=condition_transition,
        )

    @classmethod
    def creer_definition_processus(cls, nom_processus: str, description_processus: str) -> DefinitionProcessus:
        from mgl7460_tp1.implementations.traitements.definitions.definition_processus import DefinitionProcessusImpl
        return DefinitionProcessusImpl(nom=nom_processus, description=description_processus)

    @classmethod
    def creer_instance_processus(
        cls, definition_processus: DefinitionProcessus, demande_pret: DemandePret
    ) -> InstanceProcessus:
        from mgl7460_tp1.implementations.traitements.instances.instance_processus import InstanceProcessusImpl
        return InstanceProcessusImpl(definition_processus=definition_processus, demande_pret=demande_pret)

    @classmethod
    def creer_instance_tache(
        cls, definition_tache: DefinitionTache, instance_processus: InstanceProcessus
    ) -> InstanceTache:
        from mgl7460_tp1.implementations.traitements.instances.instance_tache import InstanceTacheImpl
        return InstanceTacheImpl(definition_tache=definition_tache, processus_englobant=instance_processus)
