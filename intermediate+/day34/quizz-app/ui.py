from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=50, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR, font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question = self.canvas.create_text(150, 125, text="Welcome to our Quizz", font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR, width=280)

        # Buttons
        false_image = PhotoImage(file=".\\images\\false.png")
        true_image = PhotoImage(file=".\\images\\true.png")

        self.false_button = Button(image=false_image, highlightthickness=0, command=self.press_false)
        self.false_button.grid(column=0, row=2)

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.press_true)
        self.true_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached to the end of the quizz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def press_false(self):
        is_wrong = self.quiz.check_answer("False")
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)