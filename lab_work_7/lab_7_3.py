"""
Задание 1.
Результаты сессии содержат оценки 5 экзаменов по каждой группе.
Определить средний балл для трех групп студентов одного потока и выдать
список групп в порядке убывания среднего балла. Результаты вывести в виде таблицы с заголовком.
"""

import random

class Group:
    def __init__(self, name):
        self.name = name
        self.scores = [self.generate_scores() for _ in range(5)]

    def generate_scores(self):
        return [random.randint(2, 5) for _ in range(10)]

    def calculate_average_score(self):
        total_score = sum(score for exam in self.scores for score in exam)
        total_exams = len(self.scores) * len(self.scores[0])
        return total_score / total_exams

class Stream:
    def __init__(self):
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def calculate_average_scores(self):
        results = [(group.name, group.calculate_average_score()) for group in self.groups]
        return sorted(results, key=lambda x: x[1], reverse=True)

stream = Stream()

group1 = Group("Группа A")
group2 = Group("Группа B")
group3 = Group("Группа C")

stream.add_group(group1)
stream.add_group(group2)
stream.add_group(group3)

results = stream.calculate_average_scores()

print("Результаты средних баллов по группам:")
print(f"{'Группа':<10} {'Средний балл':<15}")
print("-" * 24)
for name, avg_score in results:
    print(f"{name:<10} {avg_score:.2f}")
