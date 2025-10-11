from mgl7460_tp1.types.modeles.resultat import Resultat
from mgl7460_tp1.types.modeles.resultat_traitement import ResultatTraitement


class ResultatTraitementImpl(ResultatTraitement):

    def __init__(self, resultat: Resultat, messages: list[str] | None = None) -> None:
        self.resultat = resultat
        self.messages = messages if messages is not None else []

    def get_resultat(self) -> Resultat:
        return self.resultat

    def set_resultat(self, resultat: Resultat) -> None:
        self.resultat = resultat

    def get_messages(self) -> list[str]:
        return self.messages

    def ajouter_message(self, message: str) -> None:
        self.messages.append(message)
