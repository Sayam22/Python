import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock, Paper, Scissors")
        
        self.user_score = 0
        self.computer_score = 0
        
        self.instructions = tk.Label(master, text="Choose Rock, Paper, or Scissors:", font=("Arial", 14))
        self.instructions.pack()

        self.button_frame = tk.Frame(master)
        self.button_frame.pack()

        self.rock_button = tk.Button(self.button_frame, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack(side=tk.LEFT)

        self.paper_button = tk.Button(self.button_frame, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack(side=tk.LEFT)

        self.scissors_button = tk.Button(self.button_frame, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack(side=tk.LEFT)

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack()

        self.score_label = tk.Label(master, text="Score: You 0 - Computer 0", font=("Arial", 14))
        self.score_label.pack()

        self.play_again_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.play_again_button.pack()
        self.play_again_button.config(state=tk.DISABLED)

    def play(self, user_choice):
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        result = self.determine_winner(user_choice, computer_choice)
        
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
        self.update_score(result)
        
        self.play_again_button.config(state=tk.NORMAL)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "You lose!"

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "You lose!":
            self.computer_score += 1
        self.score_label.config(text=f"Score: You {self.user_score} - Computer {self.computer_score}")

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score: You 0 - Computer 0")
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
