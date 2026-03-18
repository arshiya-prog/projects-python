from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
score = 0
q_num = 1

for q in question_data:
    question = Question(q["text"], q["answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print()
print("You've completed the quiz!")
print(f"You final score: {quiz_brain.score}/{quiz_brain.question_number}")
print()