from question_model import Question
import requests
from quiz_brain import QuizBrain
from ui import QuizInterface


response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
response.raise_for_status()
data = response.json()['results']


question_bank = []


for question in data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(text=question_text, answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


#while quiz.still_has_questions():
    #quiz.next_question()


print("You completed the Quiz!")
print(f"Your final score was: {quiz.score} / {quiz.question_number}")