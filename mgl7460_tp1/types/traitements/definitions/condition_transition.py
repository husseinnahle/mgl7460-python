from typing import Callable

from mgl7460_tp1.types.modeles.demande_pret import DemandePret

class ConditionTransition:

    from mgl7460_tp1.types.traitements.instances.instance_tache import InstanceTache  # circular import

    def __init__(self, condition: Callable[[InstanceTache, DemandePret], bool]) -> None:
        self.condition = condition

    def is_transition_ok(self, tache_source: InstanceTache, demande_pret: DemandePret) -> bool:
        return self.condition(tache_source, demande_pret)
