from mgl7460_tp1.types.traitements.definitions.condition_transition import ConditionTransition
from mgl7460_tp1.types.traitements.definitions.definition_processus import DefinitionProcessus
from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.definitions.definition_transition import DefinitionTransition
from mgl7460_tp1.types.traitements.utils.fabrique import Fabrique


class DefinitionProcessusImpl(DefinitionProcessus):

    def __init__(self, nom: str, description: str) -> None:
        self.nom = nom
        self.description = description
        self.premiere_tache: DefinitionTache | None = None
        self.taches: list[DefinitionTache] = []
        self.transitions: list[DefinitionTransition] = []

    def get_nom(self) -> str:
        return self.nom

    def get_description(self) -> str:
        return self.description

    def set_description(self, description: str) -> None:
        self.description = description

    def get_premiere_tache(self) -> DefinitionTache | None:
        return self.premiere_tache

    def set_premiere_tache(self, tache: DefinitionTache) -> None:
        self.premiere_tache = tache

    def get_taches(self) -> list[DefinitionTache]:
        return self.taches

    def get_transitions(self) -> list[DefinitionTransition]:
        return self.transitions

    def ajouter_tache(self, definition_tache: DefinitionTache) -> None:
        self.taches.append(definition_tache)

    def ajouter_transition(self, definition_transition: DefinitionTransition) -> None:
        self.transitions.append(definition_transition)

    def ajouter_transition_entre_taches(
        self,
        tache_source: DefinitionTache,
        tache_destination: DefinitionTache,
        condition_transition: ConditionTransition,
    ) -> None:
        fabrique = Fabrique.get_singleton_fabrique()
        transition = fabrique.creer_definition_transition(
            tache_source, tache_destination, condition_transition
        )
        self.ajouter_transition(transition)

    def get_transitions_sortantes_de(
        self, tache: DefinitionTache
    ) -> list[DefinitionTransition]:
        return [t for t in self.transitions if t.get_tache_source() == tache]

    def ajouter_premiere_tache(self, tache: DefinitionTache) -> None:
        self.ajouter_tache(tache)
        self.set_premiere_tache(tache)

    def is_tache_finale(self, tache: DefinitionTache) -> bool:
        return self.get_transitions_sortantes_de(tache) == []
