class TermesPret:

    def __init__(self, amortissement: int, taux_interet: float):
        self.amortissement = amortissement
        self.taux_interet = taux_interet

    def get_amortissement(self) -> int:
        return self.amortissement

    def get_taux_interet(self) -> float:
        return self.taux_interet
