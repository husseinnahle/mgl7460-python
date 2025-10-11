from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.instances.instance_processus import InstanceProcessus


class ExceptionDefinitionProcessus(Exception):

    def __init__(
        self,
        instance_processus: InstanceProcessus,
        candidates: list[DefinitionTache],
        message: str,
    ) -> None:
        super().__init__(message)
        self.instance_processus = instance_processus
        self.prochaines_taches_candidates = candidates

    def get_instance_processus(self) -> InstanceProcessus:
        return self.instance_processus

    def get_prochaines_taches_candidates(self) -> list[DefinitionTache]:
        return [e for e in self.prochaines_taches_candidates]
