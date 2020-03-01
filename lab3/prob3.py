import random

class Elev:
    counter = 0

    def __init__(self, nume=None, sanatate=90, inteligenta=20, oboseala=0, buna_dispozitie=100):
        self.nume = "Necunostcut_" + str(Elev.counter) if nume is None else nume
        self.sanatate = sanatate
        self.inteligenta = inteligenta
        self.oboseala = oboseala
        self.bun_dispozitie = buna_dispozitie
        self.current_activity = None
        self.executed_time = 0
        self.activites = dict()
        self.is_active = True
        self.coeficient = 1.0
        Elev.counter += 1

    def apply_activity(self, activity):
        self.activites[activity.nume] = 0
        self.current_activity = activity
        self.executed_time = 0

    def execute_activity(self):
        self.executed_time += 1
        self.activites[self.current_activity.name] += 1

        self.sanatate -= self.current_activity.factor_sanatate / self.current_activity.durata
        self.inteligenta += self.current_activity.factor_inteligenta / self.current_activity.durata * self.coeficient
        self.oboseala += self.current_activity.factor_oboseala / self.current_activity.durata * self.coeficient
        self.bun_dispozitie += self.current_activity.factor_dispozitie / self.current_activity.durata * self.coeficient

        return self.executed_time <= self.current_activity.durata

    def is_final(self):
        if not (0 < self.sanatate < 100):
            return False

        if not (0 < self.inteligenta < 100):
            return False

        if not (0 < self.oboseala < 100):
            return False

        if not (0 < self.bun_dispozitie < 100):
            return False

        return True

    def get_state(self):
        if self.sanatate <= 0 or self.bun_dispozitie <= 0:
            self.is_active = False
            return "Elevul e bolnav"
        if self.oboseala >= 0:
            self.coeficient = 0.5
        else:
            self.coeficient = 1.0

    def show_activities(self):
        for key, value in self.activites.items():
            print("activity={} executat={}".format(key, value))


class Activitate:

    def __init__(self, nume, factor_sanatate, factor_inteligenta, factor_oboseala, factor_dispozitie, durata):
        self.durata = durata
        self.factor_dispozitie = factor_dispozitie
        self.factor_oboseala = factor_oboseala
        self.factor_inteligenta = factor_inteligenta
        self.factor_sanatate = factor_sanatate
        self.nume = nume

    def __str__(self):
        return "durata={} dispozitie={} oboseala={}, inteligenta={}, santate={}, nume={}".format(self.durata,
                                                                                                 self.factor_dispozitie,
                                                                                                 self.factor_inteligenta,
                                                                                                 self.factor_oboseala,
                                                                                                 self.factor_sanatate,
                                                                                                 self.nume)


activities = []
students = []
current_time = 9
pause_time = 9
if __name__ == '__main__':
    with open("activities.in") as fin:
        for line in fin.readlines():
            line = line[:-1]
            activities.append(Activitate(*line.split(" ")))

    students.append(Elev("Ionel"))
    students.append(Elev("Gigel"))
    students.append(Elev("Simona"))

    while True:
        nr = int(input("ore de afisat="))
        pause_time = current_time + nr
        while current_time < pause_time:
            for student in students:
                student.apply_activity(random.choice())


