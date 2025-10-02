from mgl7460_tp1.types.traitements.definitions.condition_transition import ConditionTransition
from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.definitions.definition_transition import DefinitionTransition


class DefinitionTransitionImpl(DefinitionTransition):

    def __init__(
        self,
        tache_source: DefinitionTache,
        tache_destination: DefinitionTache,
        condition_transition: ConditionTransition,
    ):
        self._tache_source = tache_source
        self._tache_destination = tache_destination
        self._condition_transition = condition_transition

    def get_tache_source(self) -> DefinitionTache:
        return self._tache_source

    def get_tache_destination(self) -> DefinitionTache:
        return self._tache_destination

    def get_condition_transition(self) -> ConditionTransition:
        return self._condition_transition
