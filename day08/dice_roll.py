import tkinter as tk
import random

# Dice display: 
def draw_dots(die_number, value):
    canvas.delete(f"dice{die_number}")
    dot_coords = {
        1: [(50, 50)],
        2: [(30, 30), (70, 70)],
        3: [(30, 30), (50, 50), (70, 70)],
        4: [(30, 30), (30, 70), (70, 30), (70, 70)],
        5: [(30, 30), (30, 70), (70, 30), (70, 70), (50, 50)],
        6: [(30, 30), (30, 50), (30, 70), (70, 30), (70, 50), (70, 70)],
    }
    x_offset = 0 if die_number == 1 else 100
    y_offset = 0  
    for x, y in dot_coords[value]:
        canvas.create_oval(
            x + x_offset - 5,
            y + y_offset - 5,
            x + x_offset + 5,
            y + y_offset + 5,
            fill="black",
            tags=f"dice{die_number}"
        )

# Draw numbers:
def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    draw_dots(1, die1)
    draw_dots(2, die2)
    total = die1 + die2
    result_label.config(text=f"The dice total is: {total}")

# Result Display:
def update_result_message(message, correct=False):
    result_label.config(
        text=message,
        font=("Helvetica", 14, "bold"),
        fg="white",
        bg="green" if correct else "red", 
        width=30,  
        height=2,  
        padx=10,  
        pady=10   
    )

# Handle guess:
def submit_guess():
    try:
        guess = int(guess_entry.get())
        if guess < 2 or guess > 12:
            update_result_message("Guess must be between 2 and 12.", correct=False)
            return
        roll_dice()
        total = int(result_label.cget("text").split(": ")[1])
        if guess == total:
            update_result_message(f"Correct! You guessed the total of {total}!", correct=True)
        else:
            update_result_message(f"Wrong! The total was {total}. Try again!", correct=False)
    except ValueError:
        update_result_message("Please enter a valid number.", correct=False)

# Application window
window = tk.Tk()
window.title("Guess the dice roll!")
window.geometry("400x400")

instructions = tk.Label(window, text="Guess the total of two dice (2–12):")
instructions.config(font=("Helvetica", 12))
instructions.pack(pady=20)

guess_entry = tk.Entry(window, font=("Helvetica", 14))
guess_entry.pack(pady=10)

submit_button = tk.Button(window, text="Submit Guess",  font=("Helvetica", 14), command=submit_guess)
submit_button.pack(pady=10)

canvas = tk.Canvas(window, width=200, height=100, bg="white")
canvas.pack(pady=20)

canvas.create_rectangle(20, 20, 80, 80, fill="white", outline="black")
canvas.create_rectangle(120, 20, 180, 80, fill="white", outline="black")

result_label = tk.Label(window, text="", font=("Helvetica", 10), width=30, height=2)
result_label.pack(pady=10)

window.mainloop()
