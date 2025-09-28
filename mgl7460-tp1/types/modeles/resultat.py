from enum import Enum


class Resultat(str, Enum):
    NONDETERMINE = "Non déterminée"
    ACCEPTEE = "Acceptée"
    REFUSEE = "Refusée"
