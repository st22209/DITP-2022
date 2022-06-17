import os

import random
from rich.console import Console

c = Console()

user_choice = c.input(
    "[bold blue]Rock Paper Scissors![/]\n[red]Enter rock, paper or scissors: "
)
cpu_choice = random.randint(1, 3)

match cpu_choice:
    case 1:
        cpu_choice = "rock"
    case 2:
        cpu_choice = "scissors"
    case 3:
        cpu_choice = "paper"

rps = user_choice.lower()
if rps in ["rock", "r", "1"]:
    match cpu_choice:
        case "rock":
            say = "It's a tie!"
        case "scissors":
            say = "You win!"
        case paper:
            say = "You lose!"

elif rps in ["scissors", "s", "2"]:
    match cpu_choice:
        case "scissors":
            say = "It's a tie!"
        case "paper":
            say = "You win!"
        case "rock":
            say = "You lose!"

elif rps in ["paper", "p", "3"]:
    match cpu_choice:
        case "paper":
            say = "It's a tie!"
        case "rock":
            say = "You win!"
        case "scissors":
            say = "You lose!"
else:
    say = "Invalid Input\nGet good skill issue"
    exit(0)

os.system("clear")

c.print(f"[yellow]User Choice: {user_choice}")
c.print(f"[red]Bot Choice: {cpu_choice}")
c.print(f"[green bold]{say}")
