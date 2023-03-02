from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.THEME_COLOR = "#375362"
        self.QUESTION_FONT = ('Arial', 20, 'italic')
        self.window.config(pady=20, padx=20, bg=self.THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=self.THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(bg='white', width=300, height=250)
        self.question_text = self.question_canvas.create_text(150, 125, text='something', font=self.QUESTION_FONT, width=280)
        self.question_canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # btn
        true_btn_path = PhotoImage(file='./Images/true.png')
        self.true_btn = Button(image=true_btn_path, highlightthickness=0, command=self.answer_is_true)
        self.true_btn.grid(column=0, row=2)

        false_btn_path = PhotoImage(file='./Images/false.png')
        self.false_btn = Button(image=false_btn_path, highlightthickness=0, command=self.answer_is_false)
        self.false_btn.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.question_canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.question_canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')

    def answer_is_true(self):
        user_answer = 'True'
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def answer_is_false(self):
        user_answer = 'False'
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question_canvas.config(bg='green')
        else:
            self.question_canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
