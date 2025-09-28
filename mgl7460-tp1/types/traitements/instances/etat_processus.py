from mgl7460.tp1.types.traitements.instances.etat_traitement import EtatTraitement
from mgl7460.tp1.types.traitements.instances.instance_tache import InstanceTache


class EtatProcessus:

    def __init__(self, tache_courante: InstanceTache, etat_traitement: EtatTraitement) -> None:
        self.tache_courante = tache_courante
        self.etat_traitement = etat_traitement
