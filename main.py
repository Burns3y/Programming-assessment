"""Quiz assessment - general knowledge questions."""
from tkinter import *
from tkinter import messagebox


class GUI:
    """Creating the basic GUI for the quiz."""

    def __init__(self, parent):
        """Create the GUI."""
        self.parent = parent


class PlayerScore:
    """Stores the number of questions the player answered correctly and the questions they got wrong."""

    def __init__(self, name):
        """Create and store the player's data such as name, number of correct answers and incorrect questions."""
        self.name = name
        self.correct_answers = 0
        self.incorrect_questions = []


if __name__ == "__main__":
    root = Tk()
    root.title("Quiz")
    gui = GUI(root)
    root.mainloop()
    