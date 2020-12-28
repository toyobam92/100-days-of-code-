# This is a sample Python script.
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for i in question_data:
    text = i["text"]
    answer = i["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
# print(quiz)
# print(quiz.next_question())

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was:{quiz.score}/{len(question_bank)}")





