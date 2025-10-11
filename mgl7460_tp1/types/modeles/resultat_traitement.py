from typing import Protocol

from mgl7460_tp1.types.modeles.resultat import Resultat


class ResultatTraitement(Protocol):

    def get_resultat(self) -> Resultat: ...

    def set_resultat(self, resultat: Resultat) -> None: ...

    def get_messages(self) -> list[str]: ...

    def ajouter_message(self, message: str) -> None: ...
