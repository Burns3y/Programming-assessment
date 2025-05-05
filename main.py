"""Quiz assessment - general knowledge questions."""
from tkinter import *
from tkinter import messagebox

PURPLE1 = "#864cbf"
PURPLE2 = "#46178f"


class GUI:
    """Creating the basic GUI for the quiz."""

    def __init__(self, parent):
        """Create the GUI."""
        self.parent = parent
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
        self.answer = IntVar(self.parent)
        self.answer_frame.grid(row=2, column=0, columnspan=2)

        answer_options = [("Option 1", 1), ("Option 2", 2), ("Option 3", 3), ("Option 4", 4)]
        self.answer_buttons = []
        for option_name, answer_val in answer_options:
            answer_option = Radiobutton(self.answer_frame, variable=self.answer, value=answer_val, text=option_name, bg=PURPLE2, fg="white", selectcolor=PURPLE1, activebackground=PURPLE1, activeforeground="white")
            answer_option.grid(row=(answer_val - 1) // 2, column=(answer_val - 1) % 2, sticky="w")

        #Control buttons
        self.control_frame = Frame(self.parent, bg=PURPLE2)
        self.control_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.submit_button = Button(self.control_frame, text="Submit", bg=PURPLE1, fg="white")
        self.submit_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.skip_button = Button(self.control_frame, text="Skip", command=self.skip_question, bg=PURPLE1, fg="white")
        self.restart_button = Button(self.control_frame, text="Restart", command=self.restart_quiz, bg=PURPLE1, fg="white")

        self.skip_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        self.restart_button.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    def skip_question(self):
        pass

    def restart_quiz(self):
        pass


class PlayerScore:
    """Stores the number of questions the player answered correctly
        and the questions they got wrong."""

    def __init__(self, name):
        """Create and store the player's data such as name,
            number of correct answers and incorrect questions.
            
            Also store the questions and answers."""


        self.questions = {
            "What is the chemical symbol for gold?": ["Au", "Ag", "Fe", "Pb", "Au"],
            "What is the smallest prime number?": ["1", "2", "3", "4", "2"],
            "What is the speed of light?": ["300,000 km/s", "150,000 km/s", "450,000 km/s", "600,000 km/s", "300,000 km/s"],
            "What is the currency of Japan?": ["Yen", "Won", "Dollar", "Euro", "Yen"],
            "What is the tallest mountain in the world?": ["K2", "Kilimanjaro", "Everest", "Denali", "Everest"],
            "What is the largest ocean on Earth?": ["Atlantic", "Indian", "Arctic", "Pacific", "Pacific"],
            "What is the capital of Australia?": ["Sydney", "Canberra", "Melbourne", "Brisbane", "Canberra"],
            "What is the most spoken language in the world?": ["English", "Mandarin", "Spanish", "Hindi", "Mandarin"],
            "What is the most widely used programming language?": ["Python", "Java", "C++", "JavaScript", "Python"],
            "What is the largest organ in the human body?": ["Heart", "Liver", "Skin", "Brain", "Skin"],
            "How many unique colours does the flag of South Africa have?": ["3", "4", "5", "6", "6"],
            "What is the capital of Switzerland?": ["Zurich", "Bern", "Geneva", "Lausanne", "Bern"],
            "When was the first manned moon landing?": ["1969", "1970", "1968", "1971", "1969"],
            "Who painted the Mona Lisa?": ["Vincent Van Gogh", "Picasso", "Leonardo Da Vinci", "Leonardo DiCaprio", "Da Vinci"],
            "What is the largest country in the world by land mass?": ["USA", "China", "Russia", "Canada", "Russia"],
            "What is the capital of Mongolia?": ["Ulaanbaatar", "Beijing", "Seoul", "Tokyo", "Ulaanbaatar"],
            "What is the chemical symbol for potassium?": ["K", "P", "Na", "Ca", "K"],
            "What is the largest volcano in the world?": ["Mauna Loa", "Kilimanjaro", "Mount Fuji", "Mount St. Helens", "Mauna Loa"],
            "What is the capital of Iceland?": ["Reykjavik", "Oslo", "Copenhagen", "Helsinki", "Reykjavik"],
            "what is the largest island in the world?": ["Greenland", "Australia", "New Guinea", "Borneo", "Greenland"],
            "When were women first allowed to vote in New Zealand?": ["1893", "1902", "1910", "1920", "1893"],
            "What is the capital of Canada?": ["Toronto", "Ottawa", "Vancouver", "Montreal", "Ottawa"],
            "When was the first email sent?": ["1971", "1980", "1990", "2000", "1971"],
            "Who was the first person to reach the South Pole?": ["Roald Amundsen", "Robert Falcon Scott", "Ernest Shackleton", "Ferdinand Magellan", "Roald Amundsen"],
            "When was the first photograph taken?": ["1826", "1839", "1840", "1850", "1826"],
}
        self.name = name
        self.correct_answers = 0
        self.incorrect_questions = []


if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    gui = GUI(root)
    root.mainloop()
