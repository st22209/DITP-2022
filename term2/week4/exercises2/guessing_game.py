import random

ANSWER = random.randint(1, 100)

responses = [
    "get good",
    "skill issue",
    "bad",
    "dog water",
    "trash",
    "bad",
    "imagine not guessing right",
    "tbh sounds like a skill issue",
    "lmao bad get good",
]


def check_answer(num):
    if num == ANSWER:
        return True
    elif num > ANSWER:
        print("The number you guessed is too high! {}".format(random.choice(responses)))
    elif num < ANSWER:
        print("The number you guessed is too low! {}".format(random.choice(responses)))
    return False


guess_count = 9
while guess_count > -1:
    try:
        user_guess = int(input("> "))
    except ValueError:
        print("Number must be an int! {}".format(random.choice(responses)))
        continue

    if check_answer(user_guess):
        print("Yay you guessed it!")
        break

    print(
        "You have {} guesses remaining! {}".format(
            guess_count, random.choice(responses)
        )
    )
    guess_count -= 1
else:
    print(
        "Imagine loosing, you dont have to cause you did.\n{}".format(
            random.choice(responses)
        )
    )
