from typing import Protocol

from mgl7460_tp1.types.traitements.definitions.condition_transition import ConditionTransition
from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache


class DefinitionTransition(Protocol):

    def get_tache_source(self) -> DefinitionTache: ...

    def get_tache_destination(self) -> DefinitionTache: ...

    def get_condition_transition(self) -> ConditionTransition | None: ...
