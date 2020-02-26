class Elev:
    counter = 0

    def __init__(self, nume=None, sanatate=90, inteligenta=20, oboseala=0, buna_dispozitie=100):
        self.nume = "Necunostcut_" + str(Elev.counter) if nume is None else nume
        self.sanatate = sanatate
        self.inteligenta = inteligenta
        self.oboseala = oboseala
        self.bun_dispozitie = buna_dispozitie
        Elev.counter += 1


class Activitate:

    def __init__(self, nume, factor_sanatate, factor_inteligenta, factor_oboseala, factor_dispozitie, durata):
        self.durata = durata
        self.factor_dispozitie = factor_dispozitie
        self.factor_oboseala = factor_oboseala
        self.factor_inteligenta = factor_inteligenta
        self.factor_sanatate = factor_sanatate
        self.nume = nume
