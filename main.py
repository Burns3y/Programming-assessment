"""Quiz assessment - general knowledge questions."""
from tkinter import *
from tkinter import messagebox
import functions as f
import random

COLOUR1 = "#864cbf"
COLOUR2 = "#46178f"
PADX = 10
PADY = 10
TOTAL_QUESTIONS = 10


class GUI:
    """Creating the basic GUI for the quiz.

    Logically deals with:
    Displaying questions
    Ensuring correct number of questions left
    Starting/finishing the quiz.
    """

    def __init__(self, parent, player):
        """Create the GUI."""
        self.parent = parent
        self.player = player
        self.parent.config(bg=COLOUR2)

        # Bind Enter key to submit
        self.parent.bind("<Return>", self.submit_answer)

        # Start
        self.start_quiz()

    def skip_question(self):
        """Skip the current question."""
        # Adds skipped question to the skipped questions list
        self.options.append(self.player.correct_answer)
        self.player.skipped_questions[self.question_num] = [self.question, self.options]

        # Shows next question
        messagebox.showinfo("Question Skipped", "You skipped the question.")
        self.question_num += 1
        self.display_question()
        self.question_number_label.config(text=f"Question {self.question_num}")

        # If there are no more questions left moves to the skipped questions
        if self.question_num >= TOTAL_QUESTIONS:
            self.check_skipped_questions()

        print(self.player.skipped_questions)

    def start_quiz(self):
        """Set up basic quiz GUI."""
        # Removes everything from the window
        for widget in self.parent.winfo_children():
            widget.destroy()
        
        self.player.questions = f.questions.copy()

        # Question number
        self.question_num = 1
        self.player.correct_answers = 0
        self.player.skipped_questions = {}
        self.answering_skipped = False

        # Title section
        self.title_frame = Frame(self.parent, bg=COLOUR1)
        self.title_frame.grid(row=0, column=0, columnspan=2, sticky="nesw")
        self.title_frame.columnconfigure(0, weight=1)
        self.title_label = Label(self.title_frame, text="QUIZ", bg=COLOUR1, fg="white", font=("Arial", 20))
        self.title_label.grid(row=0, column=0, sticky="ew")

        # Where the questions will be displayed
        self.question_frame = Frame(self.parent, bg=COLOUR2)
        self.question_frame.grid(row=1, column=0, columnspan=2, padx=PADX, pady=PADY)
        self.question_frame.columnconfigure(0, weight=1)

        self.question_number_label = Label(self.question_frame, text="Question 1", bg=COLOUR2, fg="white")
        self.questions_left = Label(self.question_frame, text=f"Questions left: {TOTAL_QUESTIONS}", bg=COLOUR2, fg="white")
        self.questions_left.grid(row=0, column=1, sticky="e")
        self.question_number_label.grid(row=0, column=0, sticky="w")
        self.question_label = Label(self.question_frame, text="Question will be displayed here", bg=COLOUR2, fg="white")
        self.question_label.grid(row=1, column=0, sticky="nesw")

        # Answer options
        self.answer_frame = Frame(self.parent, bg=COLOUR2)
        self.answer = StringVar(self.parent)
        self.answer.set(0)
        self.answer_frame.grid(row=2, column=0, columnspan=2)

        self.answer_buttons = []

        # Setting up radiobuttons
        for i in range(4):
            answer_option = Radiobutton(self.answer_frame, variable=self.answer, value=i, text=f"Option {i}", bg=COLOUR2, fg="white", selectcolor=COLOUR1, activebackground=COLOUR1, activeforeground="white")
            # Formats the grid into a 2x2 layout
            answer_option.grid(row=(i) // 2, column=(i) % 2, sticky="w")
            self.answer_buttons.append(answer_option)

        # Control buttons
        self.control_frame = Frame(self.parent, bg=COLOUR2)
        self.control_frame.grid(row=3, column=0, columnspan=2, padx=PADX, pady=PADY)

        self.submit_button = Button(self.control_frame, text="Submit", command=self.submit_answer, bg=COLOUR1, fg="white")
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=PADX, pady=PADY, sticky="ew")

        self.skip_button = Button(self.control_frame, text="Skip", command=self.skip_question, bg=COLOUR1, fg="white")
        self.restart_button = Button(self.control_frame, text="Restart", command=self.start_quiz, bg=COLOUR1, fg="white")

        self.skip_button.grid(row=4, column=1, padx=PADX, pady=PADY, sticky="w")
        self.restart_button.grid(row=4, column=0, padx=PADX, pady=PADY, sticky="e")

        # Display the first question
        self.display_question()

    def display_question(self, skipped_question=False):
        """Display the question and options on the GUI.

        Get the question and answers from get_random_question() in the Player class.
        If questions have been skipped, display the skipped question.
        """
        # Configures option buttons
        if not skipped_question:
            self.question, self.options = self.player.get_random_question()
        else:
            current_skipped_question = self.player.skipped_questions.popitem()
            self.question = current_skipped_question[1][0]
            self.options = current_skipped_question[1][1]
            self.player.correct_answer = self.options[4]
            self.answering_skipped = True

        self.question_label.config(text=self.question)

        for i, button in enumerate(self.answer_buttons):
            button.config(text=self.options[i], value=self.options[i])

    def submit_answer(self, event=None):
        """Submit the answer and check if it's correct."""
        # Check if there is an answer and sets it to a variable
        selected_answer = self.answer.get()
        if selected_answer not in self.options:
            messagebox.showwarning("No answer selected", "Please select an answer.")
            return

        if selected_answer == self.player.correct_answer:
            self.player.correct_answers += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showerror("Incorrect", f"Wrong! The correct answer was {self.player.correct_answer}.")

        # Check if there are more questions left
        if self.question_num >= TOTAL_QUESTIONS:
            self.check_skipped_questions()
        # If no more skipped questions
        else:
            self.display_question()
            self.question_num += 1
            self.question_number_label.config(text=f"Question {self.question_num}")
            self.questions_left.config(text=f"Questions left: {TOTAL_QUESTIONS+1 - self.question_num}")

    def check_skipped_questions(self):
        """Check if there are any skipped questions left."""
        # If no skipped questions
        if not self.player.skipped_questions:
            messagebox.showinfo("Quiz Finished", f"You answered {self.player.correct_answers} questions correctly.")
            self.end_quiz()
        # If answering skipped questions
        elif self.answering_skipped:
            self.question_number_label.config(text="Not sure? Guess!")
            self.display_question(True)
            self.questions_left.config(text=f"Questions left: {TOTAL_QUESTIONS+1 - self.question_num}")

        else:
            self.skip_button.config(state="disabled")
            self.answering_skipped = True
            self.display_question(True)
            self.title_label.config(text="Skipped Questions")

    def end_quiz(self):
        """End the quiz and show the results."""
        for frame in (self.title_frame, self.question_frame, self.answer_frame, self.control_frame):
            frame.grid_forget()
        self.title_label = Label(self.parent, text="Quiz Finished", bg=COLOUR1, fg="white", font=("Montserrat", 20))
        self.title_label.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.score_label = Label(self.parent, text=f"You answered {self.player.correct_answers} questions correctly.", bg=COLOUR2, fg="white")
        self.score_label.grid(row=1, column=0, columnspan=2, padx=PADX, pady=PADY, sticky="ew")
        self.restart_button = Button(self.parent, text="Restart", command=self.start_quiz, bg=COLOUR1, fg="white")
        self.restart_button.grid(row=1, column=0, columnspan=2, padx=PADX, pady=PADY, sticky="ew")


class Player:
    """
    Stores the number of questions the player answered correctly.

    Stores the questions they got wrong in a list.
    """

    def __init__(self):
        """
        Create and store the player's data.

        Includes number of correct answers and incorrect questions.
        Also store the questions and answers.
        """
        self.correct_answers = 0
        self.skipped_questions = {}
        self.questions = f.questions.copy()

    def get_random_question(self):
        """Get a random question from the list of questions."""
        self.question = random.choice(list(self.questions.keys()))
        self.correct_answer = self.questions[self.question][4]
        options = self.questions[self.question][:4]

        del self.questions[self.question]
        return self.question, options


if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    player = Player()
    gui = GUI(root, player)
    root.mainloop()
