# Siddhesh Zantye
# 23/03/2022

age = int(input("How old are you: "))
if age < 18:
    print(f"You cant apply because you must be 18 years old\n{18-age} more years mate")
    quit()

year_earn = int(input("How much do you earn a year: "))

if year_earn <= 40_000:
    print(
        f"You cant apply cause you earn to less\nYou must be earning at least 40k a year ({40000 - year_earn} more a year)\n \
    Get some money bro"
    )
    quit()

if year_earn > 120_000 and age > 40:
    print("You are eligible for the platinum card")

elif year_earn > 80_000 and age > 30:
    print("You are eligible for the gold card")

elif year_earn > 40_000 and age > 18:
    print("You are eligible for the card")
