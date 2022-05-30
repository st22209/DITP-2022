import random

def guess_game() -> None:
    number = random.randint(1, 100)
    tries = 0
    while True:
        try:
            user = int(input("Enter a number from 1-100: "))
        except ValueError:
            print("Invalid Input, number be an int")
            continue

        if user == number:
            print("Yay you got it, you win!")
            return

        if user > number:
            print("Number is to high")
        elif user < number:
            print("Number is to low")

        tries += 1

        if tries >= 10:
            break

    print("Out of tries, Sounds like a skill issue")
    return


guess_game()
