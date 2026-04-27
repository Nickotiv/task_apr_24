class Question:
    def __init__(self, text, options):
        self.text = text
        self.options = options
        self.votes = {}
        self.total = 0
        for option in options:
            self.votes[option] = 0
    def vote(self, option_index):
        try:
            self.votes[((list(self.votes))[option_index])] += 1
            self.total +=1
            return True
        except:
            return False
    def get_results(self):
        return self.votes
    def total_votes(self):
        return self.total
    def winner(self):
        if sorted(list(self.votes))[-1] == sorted(list(self.votes))[-2]:
            return None
        else:
            return sorted(list(self.votes))[-1]
    
class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.voted_questions = []
    def has_voted_in(self, question_id):
        if question_id in self.add_voted_question:
            return True
        else:
            return False
    def add_voted_question(self, question_id):
        self.add_voted_question.append(question_id)

class Poll:
    def __init__(self):
        self.questions = Question
        self.participants = Participant
        self.next_question_id = 0
    def add_question(self, question):
        self.questions(question.text, question.options)
    def add_participant(self, participant):
        self.participants(participant.name, participant.email)
    def find_participant_by_email(self, email):
        for participant in self.participants:
            if email in participant:
                return participant
            else:
                return None
    def find_question_by_index(self, index):
        for question in self.questions:
            if index in question:
                return question
            else:
                return None
    def cast_vote(self, participant_email, question_index, option_index):
            for participant in self.participants:
                if participant_email in participant:
                    for question in self.questparticipantsions:
                        if question_index in question:
                            if question_index in self.participants.add_voted_question(participant, question_index):
                                return "Участник уже голосовал в этом вопросе"
                            else:
                                try:
                                    self.questions.vote(option_index)
                                    self.participants.add_voted_question(participant, question_index)
                                    return "Голос принят"
                                except:
                                    return "Неверный вариант ответа"
                                
                        else:
                            return "Вопрос не найден"
                else:
                    return "Участник не найден"
    def get_question_statistics(self, question_index):
        print(f"Вопрос: {question_index}\n")
        for option in self.questions.get_results:
            print(option)
    
# Создаём опросник
poll = Poll()

# Добавляем вопрос
q1 = Question("Какой цвет вам нравится?", ["Красный", "Синий", "Зелёный"])
poll.add_question(q1)

# Добавляем участников
alice = Participant("Алиса", "alice@mail.ru")
bob = Participant("Боб", "bob@mail.ru")
poll.add_participant(alice)
poll.add_participant(bob)

# Голосование
print(poll.cast_vote("alice@mail.ru", 0, 0))   # Алиса голосует за Красный
print(poll.cast_vote("bob@mail.ru", 0, 1))     # Боб за Синий
print(poll.cast_vote("alice@mail.ru", 0, 0))   # повторная попытка — ошибка

# Статистика
print(poll.get_question_statistics(0))
