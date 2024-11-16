#Made By Deepsky
import random
import tkinter as tk
from tkinter import messagebox

class GuessNumberApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.master.geometry("400x300")
        self.secret_number = random.randint(1, 100)
        self.guess_count = 0
        self.timer_running = False
        self.label = tk.Label(master, text="Guess a number between 1 and 100:", font=("Arial", 14))
        self.label.pack(pady=20)
        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack(pady=10)
        self.guess_button = tk.Button(master, text="Guess", command=self.guess, font=("Arial", 14))
        self.guess_button.pack(pady=5)
        self.reset_button = tk.Button(master, text="Reset", command=self.reset, font=("Arial", 14))
        self.reset_button.pack(pady=5)
        self.timer_label = tk.Label(master, text="Time left: 30 seconds", font=("Arial", 14))
        self.timer_label.pack(pady=10)
        self.start_timer()

    def start_timer(self):
        self.time_left = 60
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if  self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left} seconds")
            if self.time_left <= 10:
                bright_colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FFD733", "#FF33FF"]
                selected_color = random.choice(bright_colors)
                self.master.config(bg=selected_color)
                
            self.time_left -= 1
            self.master.after(1000, self.update_timer)
        else:
            self.timer_running = False
            self.guess_button.config(state=tk.DISABLED) 
            messagebox.showinfo("Time's Up", "Time's up! You can no longer guess.")

    def guess(self):
        if not self.timer_running:
            return

        try:
            guess = int(self.entry.get())
            self.guess_count += 1

            if guess < self.secret_number:
                messagebox.showinfo("Result", "Your guess is too low. Try again!")
            elif guess > self.secret_number:
                messagebox.showinfo("Result", "Your guess is too high. Try again!")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number {self.secret_number} in {self.guess_count} guesses.")
                self.reset()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    def reset(self):
        self.secret_number = random.randint(1, 100)
        self.guess_count = 0
        self.entry.delete(0, tk.END)
        self.guess_button.config(state=tk.NORMAL)  # Enable the "Guess" button
        self.start_timer() 

if __name__ == "__main__":
    root = tk.Tk()
    app = GuessNumberApp(root)
    root.mainloop()