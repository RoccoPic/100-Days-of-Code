from question_model import Question
from data import question_data, question_data2
from quiz_brain import QuizBrain
question_bank = []
question_bank2 = []
# for i in range(0, len(question_data)):
#     q = Question(question_data[i]["text"], question_data[i]["answer"])
#     question_bank.append(q)

for question in question_data:
    text = question["text"]
    answer = question["answer"]
    full_question = Question(text, answer)
    question_bank.append(full_question)
print(question_bank)

for question in question_data2:
    text = question["question"]
    answer = question["correct_answer"]
    full_question = Question(text, answer)
    question_bank2.append(full_question)
print(question_bank2)

quiz2 = QuizBrain(question_bank2)
while quiz2.still_has_questions():
    quiz2.next_question()

# quiz = QuizBrain(question_bank)
# while quiz.still_has_questions():
#     quiz.next_question()