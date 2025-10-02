from typing import Protocol

from mgl7460_tp1.types.modeles.demande_pret import DemandePret
# from mgl7460_tp1.types.traitements.instances.instance_tache import InstanceTache  # circular import


class ConditionTransition(Protocol):

    def is_transition_ok(self, tache_source, demande_pret: DemandePret) -> bool: ...
