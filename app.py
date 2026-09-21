import random
import tkinter as tk
from tkinter import ttk


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root

        self.root.title("Number Guessing Game")
        self.root.geometry("650x700")
        self.root.resizable(False, False)

        # Game variables
        self.number = 0
        self.attempts_left = 0
        self.max_attempts = 7
        self.previous_guesses = []

        # Difficulty settings
        self.difficulty = tk.StringVar(value="Normal")

        self.create_widgets()
        self.start_game()

    def create_widgets(self):
        # Main title
        title = tk.Label(
            self.root,
            text="🎯 NUMBER GUESSING GAME",
            font=("Arial", 24, "bold"),
        )
        title.pack(pady=20)

        # Subtitle
        subtitle = tk.Label(
            self.root,
            text="Can you discover the secret number?",
            font=("Arial", 12),
        )
        subtitle.pack()

        # Difficulty
        difficulty_frame = tk.Frame(self.root)
        difficulty_frame.pack(pady=20)

        tk.Label(
            difficulty_frame,
            text="Difficulty:",
            font=("Arial", 11, "bold"),
        ).pack(side="left", padx=5)

        difficulty_menu = ttk.Combobox(
            difficulty_frame,
            textvariable=self.difficulty,
            values=["Easy", "Normal", "Hard"],
            state="readonly",
            width=10,
        )
        difficulty_menu.pack(side="left")
        difficulty_menu.bind("<<ComboboxSelected>>", self.change_difficulty)

        # Range information
        self.range_label = tk.Label(
            self.root,
            text="I selected a number between 1 and 100.",
            font=("Arial", 13),
        )
        self.range_label.pack(pady=10)

        # Attempts
        self.attempt_label = tk.Label(
            self.root,
            text="Attempts Remaining: 7",
            font=("Arial", 14, "bold"),
        )
        self.attempt_label.pack(pady=10)

        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=400,
            mode="determinate",
        )
        self.progress.pack(pady=5)

        # Guess input
        tk.Label(
            self.root,
            text="Enter your guess:",
            font=("Arial", 13, "bold"),
        ).pack(pady=(30, 5))

        self.guess_entry = tk.Entry(
            self.root,
            font=("Arial", 18),
            justify="center",
            width=12,
        )
        self.guess_entry.pack(pady=10)
        self.guess_entry.bind("<Return>", lambda event: self.check_guess())

        self.guess_button = tk.Button(
            self.root,
            text="SUBMIT GUESS",
            font=("Arial", 12, "bold"),
            width=18,
            command=self.check_guess,
        )
        self.guess_button.pack(pady=10)

        # Feedback
        self.feedback_label = tk.Label(
            self.root,
            text="Make your first guess!",
            font=("Arial", 15, "bold"),
        )
        self.feedback_label.pack(pady=25)

        self.distance_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
        )
        self.distance_label.pack()

        # Previous guesses
        self.history_label = tk.Label(
            self.root,
            text="Previous guesses: None",
            font=("Arial", 11),
            wraplength=550,
        )
        self.history_label.pack(pady=25)

        # Score
        self.score_label = tk.Label(
            self.root,
            text="Score: 0",
            font=("Arial", 13, "bold"),
        )
        self.score_label.pack(pady=5)

        # Restart
        restart_button = tk.Button(
            self.root,
            text="🔄 NEW GAME",
            font=("Arial", 11, "bold"),
            width=16,
            command=self.start_game,
        )
        restart_button.pack(pady=20)

    def change_difficulty(self, event=None):
        self.start_game()

    def start_game(self):
        difficulty = self.difficulty.get()

        if difficulty == "Easy":
            self.minimum = 1
            self.maximum = 50
            self.max_attempts = 10
        elif difficulty == "Normal":
            self.minimum = 1
            self.maximum = 100
            self.max_attempts = 7
        else:
            self.minimum = 1
            self.maximum = 200
            self.max_attempts = 6

        self.number = random.randint(self.minimum, self.maximum)
        self.attempts_left = self.max_attempts
        self.previous_guesses = []

        # Reset GUI
        self.range_label.config(
            text=f"I selected a number between {self.minimum} and {self.maximum}."
        )
        self.attempt_label.config(
            text=f"Attempts Remaining: {self.attempts_left}"
        )
        self.progress["maximum"] = self.max_attempts
        self.progress["value"] = self.attempts_left
        self.feedback_label.config(text="Make your first guess!")
        self.distance_label.config(text="")
        self.history_label.config(text="Previous guesses: None")
        self.score_label.config(text="Score: 0")

        # Enable before clearing so restart also works after the game ends.
        self.guess_entry.config(state="normal")
        self.guess_entry.delete(0, tk.END)
        self.guess_button.config(state="normal")
        self.guess_entry.focus()

    def check_guess(self):
        guess_text = self.guess_entry.get().strip()

        if guess_text == "":
            self.feedback_label.config(text="⚠️ Enter a number first.")
            return

        try:
            guess = int(guess_text)
        except ValueError:
            self.feedback_label.config(text="❌ Please enter a valid integer.")
            self.guess_entry.delete(0, tk.END)
            return

        if guess < self.minimum or guess > self.maximum:
            self.feedback_label.config(
                text=f"⚠️ Enter a number between {self.minimum} and {self.maximum}."
            )
            self.guess_entry.delete(0, tk.END)
            return

        if guess in self.previous_guesses:
            self.feedback_label.config(text=f"⚠️ You already guessed {guess}.")
            self.guess_entry.delete(0, tk.END)
            return

        self.previous_guesses.append(guess)
        self.history_label.config(
            text="Previous guesses: " + ", ".join(map(str, self.previous_guesses))
        )

        if guess == self.number:
            attempts_used = self.max_attempts - self.attempts_left + 1
            score = self.calculate_score(attempts_used)

            self.feedback_label.config(text="🎉 CORRECT! YOU WON!")
            self.distance_label.config(text=f"The secret number was {self.number}.")
            self.score_label.config(text=f"🏆 Score: {score}")
            self.end_game()
            return

        self.attempts_left -= 1
        self.attempt_label.config(
            text=f"Attempts Remaining: {self.attempts_left}"
        )
        self.progress["value"] = self.attempts_left

        if self.attempts_left == 0:
            self.feedback_label.config(text="💀 GAME OVER")
            self.distance_label.config(text=f"The correct number was {self.number}.")
            self.end_game()
            return

        if guess < self.number:
            direction = "⬆️ Too Low! Guess higher."
        else:
            direction = "⬇️ Too High! Guess lower."

        difference = abs(self.number - guess)
        if difference <= 3:
            distance = "🔥 Extremely close!"
        elif difference <= 10:
            distance = "🔥 Very close!"
        elif difference <= 20:
            distance = "🙂 You're getting close."
        elif difference <= 40:
            distance = "❄️ You're quite far."
        else:
            distance = "🥶 Very far away!"

        self.feedback_label.config(text=direction)
        self.distance_label.config(text=distance)
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus()

    @staticmethod
    def calculate_score(attempts_used):
        base_score = 1000
        penalty = (attempts_used - 1) * 100
        return max(base_score - penalty, 100)

    def end_game(self):
        self.guess_entry.config(state="disabled")
        self.guess_button.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
