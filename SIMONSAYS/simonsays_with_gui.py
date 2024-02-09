import tkinter as tk
from tkinter import messagebox
import random

class SimonSaysGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Simon Says")
        self.commands = ["Simon says jump", "Simon says clap", "Simon says nod", "Jump", "Clap", "Nod"]
        self.current_command = ""
        
        self.label = tk.Label(master, text="Simon Says Game")
        self.label.pack()
        
        self.command_label = tk.Label(master, text="")
        self.command_label.pack()
        
        self.input_entry = tk.Entry(master)
        self.input_entry.pack()
        
        self.submit_button = tk.Button(master, text="Submit", command=self.check_command)
        self.submit_button.pack()
        
        self.new_command()
        
    def new_command(self):
        self.current_command = random.choice(self.commands)
        self.command_label.config(text=self.current_command)
        
    def check_command(self):
        user_input = self.input_entry.get().strip().lower()
        correct_answer = self.current_command[11:].strip().lower() if self.current_command.startswith("Simon says") else self.current_command.strip().lower()
        
        if user_input == correct_answer:
            messagebox.showinfo("Correct", "Good job!")
        else:
            messagebox.showerror("Wrong", "Game Over.")
            self.master.destroy()
        
        self.new_command()

def main():
    root = tk.Tk()
    game = SimonSaysGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
