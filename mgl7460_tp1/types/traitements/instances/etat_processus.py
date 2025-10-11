from mgl7460_tp1.types.traitements.instances.etat_traitement import EtatTraitement
from mgl7460_tp1.types.traitements.instances.instance_tache import InstanceTache


class EtatProcessus:

    def __init__(
        self, tache_courante: InstanceTache | None, etat_traitement: EtatTraitement
    ) -> None:
        self.tache_courante = tache_courante
        self.etat_traitement = etat_traitement

    def get_tache_courante(self) -> InstanceTache | None:
        return self.tache_courante

    def get_etat_traitement(self) -> EtatTraitement:
        return self.etat_traitement
