from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for item in question_data:
    question = Question(item['question'],item['correct_answer'])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
quiz_brain.next_question()

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz_brain.score}/{len(quiz_brain.q_list)}")

