"""Quiz assessment - general knowledge questions."""
from tkinter import *
from tkinter import messagebox
import functions as f
import random

PURPLE1 = "#864cbf"
PURPLE2 = "#46178f"


class GUI:
    """Creating the basic GUI for the quiz."""

    def __init__(self, parent, player):
        """Create the GUI."""
        self.parent = parent
        self.player = player
        self.parent.config(bg=PURPLE2)
        # self.answer.set(1)

        # Title section
        self.title_frame = Frame(self.parent, bg=PURPLE1)
        self.title_frame.grid(row=0, column=0, columnspan=2, sticky="nesw")
        self.title_frame.columnconfigure(0, weight=1)
        self.title_label = Label(self.title_frame, text="QUIZ", bg=PURPLE1, fg="white", font=("Montserrat", 20))
        self.title_label.grid(row=0, column=0, sticky="ew")

        # Where the questions will be displayed
        self.question_frame = Frame(self.parent, bg=PURPLE2)
        self.question_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.question_frame.columnconfigure(0, weight=1)

        self.question_number_label = Label(self.question_frame, text="Question 1", bg=PURPLE2, fg="white")
        self.questions_left = Label(self.question_frame, text="Questions left: 10", bg=PURPLE2, fg="white")
        self.questions_left.grid(row=0, column=1, sticky="e")
        self.question_number_label.grid(row=0, column=0, sticky="w")
        self.question_label = Label(self.question_frame, text="Question will be displayed here", bg=PURPLE2, fg="white")
        self.question_label.grid(row=1, column=0, sticky="nesw")

        # Answer options
        self.answer_frame = Frame(self.parent, bg=PURPLE2)
        self.answer = StringVar(self.parent)
        self.answer_frame.grid(row=2, column=0, columnspan=2)

        answer_options = [("Option 1", 1), ("Option 2", 2), ("Option 3", 3), ("Option 4", 4)]
        self.answer_buttons = []

        for option_name, answer_val in answer_options:
            answer_option = Radiobutton(self.answer_frame, variable=self.answer, value=answer_val, text=option_name, bg=PURPLE2, fg="white", selectcolor=PURPLE1, activebackground=PURPLE1, activeforeground="white")
            # Formats the grid into a 2x2 layout
            answer_option.grid(row=(answer_val - 1) // 2, column=(answer_val - 1) % 2, sticky="w")
            self.answer_buttons.append(answer_option)

        # Control buttons
        self.control_frame = Frame(self.parent, bg=PURPLE2)
        self.control_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.submit_button = Button(self.control_frame, text="Submit", command=self.submit_answer ,bg=PURPLE1, fg="white")
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.skip_button = Button(self.control_frame, text="Skip", command=self.skip_question, bg=PURPLE1, fg="white")
        self.restart_button = Button(self.control_frame, text="Restart", command=self.restart_quiz, bg=PURPLE1, fg="white")

        self.skip_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        self.restart_button.grid(row=4, column=0, padx=10, pady=10, sticky="e")

        # Display the first question
        self.display_question()


    def skip_question(self):
        """Skip the current question."""
        self.display_question()
        messagebox.showinfo("Question Skipped", "You skipped the question.")

    def restart_quiz(self):
        """Restart the quiz."""
        pass

    def display_question(self):
        '''Display the question and options on the GUI
        
        Get the question and answers from get_random_question() in the Player class.
        '''
        # Configures option buttons
        question, options = self.player.get_random_question()
        self.question_label.config(text=question)
        self.question_number_label.config(text=f"Question {self.player.correct_answers + 1}")
        
        for i, button in enumerate(self.answer_buttons):
            button.config(text=options[i], value=options[i])

    def submit_answer(self):
        print(f"Answer: {self.player.correct_answer}, Selected: {self.answer.get()}")
        """Submit the answer and check if it's correct."""
        # Check if there is an answer and sets it to a variable
        selected_answer = self.answer.get()
        if selected_answer == 0:
            messagebox.showwarning("No answer selected", "Please select an answer.")
            return

        if selected_answer == self.player.correct_answer:
            self.player.correct_answers += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            self.player.incorrect_questions.append(self.player.question)
            messagebox.showerror("Incorrect", f"Wrong! The correct answer was {self.player.correct_answer}.")

        # Check if there are more questions left
        if len(self.player.questions) > 0:
            self.display_question()
        else:
            messagebox.showinfo("Quiz Finished", f"You answered {self.player.correct_answers} questions correctly.")
            self.parent.quit()


class Player:

    """Stores the number of questions the player answered correctly
    and the questions they got wrong."""

    def __init__(self, name):
        """Create and store the player's data such as name,
            number of correct answers and incorrect questions.
            
            Also store the questions and answers."""

        self.name = name
        self.correct_answers = 0
        self.incorrect_questions = []

        self.questions = f.UsefulMethods().questions

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
    player = Player("Player")
    gui = GUI(root, player)
    root.mainloop()
