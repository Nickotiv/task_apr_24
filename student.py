class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group
        self.grades = []
        self.gradeCount = 0
    def add_grade(self, grade):
        if grade < 6:
            self.grades.append(grade)
            self.gradeCount += 1
    def average_grade(self):
        if self.gradeCount != 0:
            return (sum(self.grades) / self.gradeCount)
        else:
            return 0.0
    def info(self):
        return (f"{self.name}, группа {self.group}, средний балл: {s.average_grade()}")

s = Student("Анна", "ФИПМ_21")
s.add_grade(5)
s.add_grade(4)
s.add_grade(3)
print(s.average_grade())   # 4.0
print(s.info())            # "Анна, группа ФИПМ_21, средний балл: 4.0"

s = Student("Иван", "ФИПМ_31")
s.add_grade(5)
s.add_grade(4)
s.add_grade(6)   # неверная оценка, не должна добавиться
assert s.grades == [5, 4], "Ошибка: список оценок должен быть [5,4]"
assert s.average_grade() == 4.5, "Ошибка: среднее (5+4)/2 = 4.5"
print("Тест 1 пройден")

s = Student("Мария", "ФИПМ_11")
assert s.average_grade() == 0.0, "Ошибка: для пустого списка средний балл 0.0"
s.add_grade(5)
s.add_grade(5)
expected_info = "Мария, группа ФИПМ_11, средний балл: 5.0"
assert s.info() == expected_info, "Ошибка: неверный формат строки info"
print("Тест 2 пройден")
