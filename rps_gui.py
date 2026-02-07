import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

def play(user_choice):
    computer_choice = random.choice(choices)
    computer_label.config(text="Computer chose: " + computer_choice)

    if user_choice == computer_choice:
        result_label.config(text="Draw!", fg="yellow")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You Win!", fg="lightgreen")
    else:
        result_label.config(text="You Lose!", fg="red")


root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.configure(bg="#1e293b")   # background color

title = tk.Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 16),
    bg="#1e293b",
    fg="white"
)
title.pack(pady=10)

computer_label = tk.Label(
    root,
    text="Computer chose: ?",
    font=("Arial", 12),
    bg="#1e293b",
    fg="white"
)
computer_label.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14),
    bg="#1e293b"
)
result_label.pack(pady=10)

button_frame = tk.Frame(root, bg="#1e293b")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", bg="#3b82f6", fg="white", width=10,
                     command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", bg="#10b981", fg="white", width=10,
                      command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", bg="#ef4444", fg="white", width=10,
                         command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

root.mainloop()
