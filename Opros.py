class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options
        self.votes = {}

        for option in options:
            self.votes[option] = 0

    def vote(self, option_index):
        if option_index < 0 or option_index >= len(self.options):
            return False

        option = self.options[option_index]
        self.votes[option] += 1

        return True

    def get_results(self):
        return self.votes.copy()

    def total_votes(self):
        return sum(self.votes.values())

    def winner(self):
        max_votes = max(self.votes.values())

        winners = []

        for option, votes in self.votes.items():
            if votes == max_votes:
                winners.append(option)

        if len(winners) == 1:
            return winners[0]

        return None


class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.voted_questions = []

    def has_voted_in(self, question_id):
        return question_id in self.voted_questions

    def add_voted_question(self, question_id):
        self.voted_questions.append(question_id)


class Poll:
    def __init__(self):
        self.questions = []
        self.participants = []
        self.next_question_id = 0

    def add_question(self, question):
        self.questions.append(question)
        self.next_question_id += 1

    def add_participant(self, participant):
        self.participants.append(participant)

    def find_participant_by_email(self, email):
        for participant in self.participants:
            if participant.email == email:
                return participant

        return None

    def find_question_by_index(self, index):
        if index < 0 or index >= len(self.questions):
            return None

        return self.questions[index]

    def cast_vote(self, participant_email, question_index, option_index):
        participant = self.find_participant_by_email(participant_email)

        if participant is None:
            return "Участник не найден"

        question = self.find_question_by_index(question_index)

        if question is None:
            return "Вопрос не найден"

        if participant.has_voted_in(question_index):
            return "Участник уже голосовал в этом вопросе"

        vote_success = question.vote(option_index)

        if not vote_success:
            return "Неверный вариант ответа"

        participant.add_voted_question(question_index)

        return "Голос принят"

    def get_question_statistics(self, question_index):
        question = self.find_question_by_index(question_index)

        if question is None:
            return "Вопрос не найден"

        lines = []

        lines.append(f"Вопрос: {question.text}")

        for option, votes in question.get_results().items():
            lines.append(f"{option}: {votes} голосов")

        lines.append(f"Всего голосов: {question.total_votes()}")

        winner = question.winner()

        if winner is None:
            lines.append("Победитель: нет")
        else:
            lines.append(f"Победитель: {winner}")

        return "\n".join(lines)


poll = Poll()

q1 = Question("Какой цвет вам нравится?", ["Красный", "Синий", "Зелёный"])
poll.add_question(q1)

alice = Participant("Алиса", "alice@mail.ru")
bob = Participant("Боб", "bob@mail.ru")

poll.add_participant(alice)
poll.add_participant(bob)

print(poll.cast_vote("alice@mail.ru", 0, 0))
print(poll.cast_vote("bob@mail.ru", 0, 1))
print(poll.cast_vote("alice@mail.ru", 0, 0))

print(poll.get_question_statistics(0))

# Тест 1: создание вопроса и подсчёт голосов
q = Question("Тест?", ["A", "B"])
q.vote(0)
q.vote(0)
q.vote(1)
assert q.total_votes() == 3
assert q.winner() == "A"
assert q.get_results() == {"A": 2, "B": 1}
print("Тест 1 пройден")

# Тест 2: некорректное голосование
q2 = Question("Опрос", ["Да", "Нет"])
assert q2.vote(2) == False   # неверный индекс
assert q2.total_votes() == 0
print("Тест 2 пройден")

# Тест 3: участник не может голосовать дважды
poll = Poll()
q3 = Question("Вопрос", ["1", "2"])
poll.add_question(q3)
user = Participant("Иван", "ivan@ya.ru")
poll.add_participant(user)
res1 = poll.cast_vote("ivan@ya.ru", 0, 0)
res2 = poll.cast_vote("ivan@ya.ru", 0, 1)
assert res1 == "Голос принят"
assert "уже голосовал" in res2.lower()
print("Тест 3 пройден")

# Тест 4: поиск победителя при ничьей
q4 = Question("Ничья", ["X", "Y"])
q4.vote(0)
q4.vote(1)
assert q4.winner() is None
print("Тест 4 пройден")
