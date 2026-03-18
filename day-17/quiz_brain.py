class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.q_list = question_list

    def still_has_questions(self):
        last_index = len(self.q_list)
        return self.question_number != last_index

    def next_question(self):
        current_question = self.q_list[self.question_number]
        self.question_number += 1
        self.user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")

        self.check_answer(self.user_answer, current_question.answer)

    def check_answer(self, user_ans, actual_ans):
        if user_ans.lower() == actual_ans.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was {actual_ans}")
        print(f"Current score is: {self.score}/{self.question_number}")
        print()