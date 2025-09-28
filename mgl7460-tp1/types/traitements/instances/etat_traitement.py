from enum import Enum


class EtatTraitement(str, Enum):
    EN_COURS = "En cours"
    PRET = "Prêt"
    TERMINE = "Terminé"
