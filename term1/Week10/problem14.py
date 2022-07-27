import time, os

os.system("clear")

savings = 10

salary = float(input("How much do you get payed per week? "))
bills = float(input("How much are your bills every week? "))

weeks = 0

os.system("clear")

while savings < 2000:
    extra = salary - bills

    weeks += 1
    time.sleep(0.1)
    print(f"Week: {weeks} | Savings: {savings}", end="\r", flush=True)

    savings += extra
    time.sleep(0.1)

weeks += 1
print(f"\nSavings: {savings}\nYou can go to fiji")
print(f"\nIt took you {weeks} weeks ({round(weeks/52, 2)} years) to get to 2000")
