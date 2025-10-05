from mgl7460_tp1.types.traitements.definitions.definition_tache import DefinitionTache
from mgl7460_tp1.types.traitements.definitions.traitement_tache import TraitementTache


class DefinitionTacheImpl(DefinitionTache):

    def __init__(self, nom: str, description: str, traitement: TraitementTache | None = None) -> None:
        self._nom = nom
        self._description = description
        self._traitement = traitement

    def get_nom(self) -> str:
        return self._nom

    def get_description(self) -> str:
        return self._description

    def set_description(self, description: str) -> None:
        self._description = description

    def get_traitement_tache(self) -> TraitementTache:
        return self._traitement

    def set_traitement_tache(self, traitement: TraitementTache) -> None:
        self._traitement = traitement
