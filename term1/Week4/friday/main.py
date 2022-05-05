import sys
import random

print("Hello there!\nWhat's your name?")

name = input("> ")

print(f"Hello {name}, Hows your day going?")

day_going = input("> ")

age = int(input("How old are you?\n> "))

print("Ok\nDo you play cricket?")

yes_or_no = input("> ")

if yes_or_no.lower() not in ['yes', 'y']:
    print("Ok")
    sys.exit(0)

print("What do you like more, Bowling or batting? ")

player_type = input("> ")

print(f"Thats cool, I like {player_type} too\nHow long have you been playing (in years)")

long = int(input("> "))

if long > age:
    print(f"Thats not possible, you're only {age} years old")

high_score = int(input("What is your high score?\n> "))

print(f"Thats cool, Mines {random.randint(high_score, high_score+100)}")

print("How many people are in a team?")

team = input("> ")
if team != 11:
    print("You're wrong the answer is 11")

print("Who is your favourite player")

player = input("> ")

print("Thats cool")

print("What is your advice for other people?")
advice = input("> ")

print("Ok i will use that to be better when i play too")

print(f"It has been fun talking to you {name}\nI gotta go now but thanks for speaking to me :)")