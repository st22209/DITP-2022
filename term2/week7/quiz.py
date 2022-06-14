import os
import time
import json
import random

from rich.console import Console

console = Console()

play = console.input("[blue bold]Would you like to play? (Yes/No) ").lower()
if play not in ["yes", "y"]:
    console.print("[purple bold]ok!\n")
    quit(0)

points = 0
num = 1

with open("questions.json") as f:
    questions_and_answers_ps = json.load(f)

    shuffled_qa = list(questions_and_answers_ps.items())

    random.shuffle(shuffled_qa)

    questions_and_answers = {}

    for k, v in shuffled_qa:
        questions_and_answers[k] = v


console.print("[purple bold]Welcome to the quiz!")
console.input("[red]press any key to start...")

for question, answer in questions_and_answers.items():
    os.system("clear")
    console.print(f"[yellow]Q{num}: {question}?")
    user_ans = console.input("(true/false): ").lower()

    if user_ans in ["yes", "true", "t", "y", "1"]:
        user_ans = True
    elif user_ans in ["no", "false", "f", "n", "0"]:
        user_ans = False
    else:
        user_ans = None

    num += 1

    if user_ans == answer:
        points += 1
        console.print("[green]Correct!")
        time.sleep(1)
        continue

    console.print("[red]Wrong!")
    time.sleep(1)
    

os.system("clear")

console.print(
    f"[blue bold]The quiz is done.\nYou scored {points}/10 points and got {points * 10}% correct!"
)
