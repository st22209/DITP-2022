try:
    clothes = float(input(f"How much do you spend on Clothes: "))
    transport = float(input(f"How much do you spend on Transport: "))
    food = float(input(f"How much do you spend on Food: "))
    rent = float(input(f"How much do you spend on Rent: "))
    
    total = clothes + transport + food + rent

    print(f"Total expenses: {total}")

except ValueError as err:
    print(err)
    print("You must input numbers!")