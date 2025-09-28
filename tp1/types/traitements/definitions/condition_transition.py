
from mgl7460.tp1.types.modeles.demande_pret import DemandePret
from mgl7460.tp1.types.traitements.instances.instance_tache import InstanceTache


class ConditionTransition:

    def is_transition_ok(self, tache_source: InstanceTache, demande_pret: DemandePret) -> bool: ...
