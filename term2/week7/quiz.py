import os
import json

from rich.console import Console

console = Console()

play = console.input("[blue bold]Would you like to play? (Yes/No) ").lower()
if play not in ["yes", "y"]:
    quit(0)

points = 0
num = 1

with open("questions.json") as f:
    questions_and_answers = json.load(f)

console.print("[purple bold]Welcome to the quiz!\n")
input("press any key to start...")

for question, answer in questions_and_answers.items():
    os.system("clear")
    console.print(f"[yellow]Q{num}: {question}?")
    user_ans = console.input("(true/false): ").lower()
    user_ans = True if user_ans in ["yes", "true", "t", "y", "1"] else False

    num += 1

    if user_ans == answer:
        points += 1
        console.print("[green]Correct!")
        continue
    
    console.print("[red]Wrong!")

os.system("clear")

console.print(f"[blue bold]The quiz is done.\nYou scored {points}/10 points and got {points * 10}% correct!")