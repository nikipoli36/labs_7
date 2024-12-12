"""
Задание 2.
Составить программу для обработки результатов кросса на 500 м для женщин.
Для каждой участницы ввести фамилию, группу, фамилию преподавателя, результат.
Получить результирующую таблицу, упорядоченную по результатам, в которой содержится
также информация о выполнении норматива. Определить суммарное количество участниц, выполнивших норматив.
"""

class Participant:
    def __init__(self, last_name, group, inst, res):
        self.last_name = last_name
        self.group = group
        self.inst = inst
        self.res = res

    def meets_standard(self):
        return self.res <= 60

class Race:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def get_results(self):

        sorted_participants = sorted(self.participants, key=lambda p: p.res)
        results = []

        for participant in sorted_participants:
            standard_status = "выполнила" if participant.meets_standard() else "не выполнила"
            results.append(f"{participant.last_name}, {participant.group}, {participant.inst}, {participant.res} сек - {standard_status} норматив")
        return results

    def count_meeting_standard(self):
        return sum(1 for p in self.participants if p.meets_standard())

race = Race()

num_participants = int(input("Введите количество участниц >> "))

for _ in range(num_participants):
    last_name = input("Введите фамилию участницы >> ")
    group = int(input("Введите группу участницы >> "))
    if group % 2 == 0:
        inst = str('Петров')
    else: inst = str('Васечкин')
    res = int(input("Введите результат участницы (в секундах) >> "))

    race.add_participant(Participant(last_name, group, inst, res))

results = race.get_results()
for res in results:
    print(res)

count = race.count_meeting_standard()
print(f"Количество участниц, выполнивших норматив: {count}")