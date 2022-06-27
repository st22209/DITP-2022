money = 1000

intrest = float(input("Enter intrest rate: "))
period = int(input("Enter investment period (years): "))

for i in range(period):
    money += (money * (intrest / 100))

print(f"After {period} years your balance is: ${money:.2f}")