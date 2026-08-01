from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"



#Graphical user interface 
class QuizInterFace:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        #window
        self.window = Tk()
        self.window.title("Quiz Brain")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        #lable
        self.score = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.score.grid(column=1, row= 0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280, 
                                                     text="some question text", fill=THEME_COLOR,
                                                      font=("Arial", 20, "italic"))
        
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.cross_img = PhotoImage(file="Day-34/image/false.png")
        self.true_img = PhotoImage(file="Day-34/image/true.png")

        self.true_button = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.cross_button = Button(image=self.cross_img, highlightthickness=0, command=self.false_pressed)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions:
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.cross_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        
        self.window.after(1000, self.get_next_question)
