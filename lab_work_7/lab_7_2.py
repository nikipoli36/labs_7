"""
Задание 4.
Соревнования по прыжкам в воду оценивают 7 судей. Каждый спортсмен выполняет 4 прыжка.
Каждый прыжок имеет одну из шести категорий сложности, оцениваемую коэффициентом (от 2,5 до 3,5).
Качество прыжка оценивается судьями по 6-балльной шкале. Далее лучшая и худшая оценки отбрасываются,
остальные складываются, и сумма умножается на коэффициент сложности. Получить итоговую таблицу,
содержащую фамилии спортсменов, и итоговую оценку (сумму оценок по 4 прыжкам) в порядке занятых мест.
"""

import random

class Jump:
    def __init__(self, difficulty_coefficient):
        self.difficulty_coefficient = difficulty_coefficient
        self.scores = self.generate_scores()

    def generate_scores(self):
        return [random.randint(0, 6) for _ in range(7)]

    def calculate_score(self):
        sorted_scores = sorted(self.scores)[1:-1]
        return sum(sorted_scores) * self.difficulty_coefficient

class Athlete:
    def __init__(self, name):
        self.name = name
        self.jumps = []

    def add_jump(self, jump):
        self.jumps.append(jump)

    def calculate_total_score(self):
        total_score = sum(jump.calculate_score() for jump in self.jumps)
        return total_score

class Competition:
    def __init__(self):
        self.athletes = []

    def add_athlete(self, athlete):
        self.athletes.append(athlete)

    def run_competition(self):
        results = []
        for athlete in self.athletes:
            total_score = athlete.calculate_total_score()
            results.append((athlete.name, total_score))
        results.sort(key=lambda x: x[1], reverse=True)
        return results

competition = Competition()

ath1 = Athlete("Иванов")
ath2 = Athlete("Петров")
ath3 = Athlete("Сидоров")

for _ in range(4):
    difficulty_coefficient = random.uniform(2.5, 3.5)
    ath1.add_jump(Jump(difficulty_coefficient))
    difficulty_coefficient = random.uniform(2.5, 3.5)
    ath2.add_jump(Jump(difficulty_coefficient))
    difficulty_coefficient = random.uniform(2.5, 3.5)
    ath3.add_jump(Jump(difficulty_coefficient))

competition.add_athlete(ath1)
competition.add_athlete(ath2)
competition.add_athlete(ath3)

results = competition.run_competition()
print("Результаты соревнования >>")
for name, score in results:
    print(f"{name} >> {score:.2f}")
