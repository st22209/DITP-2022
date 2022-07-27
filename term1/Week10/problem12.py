import time, os

os.system("clear")

target = 2_000_000
# intrest_rate = 1 + 0.006

savings = float(input("How much do you have currently saved? "))
salary = float(input("How much do you get payed per week? "))
bills = float(input("How much are your bills every week? "))

weeks = 0

os.system("clear")

while savings < target:
    extra = salary - bills

    weeks += 1
    time.sleep(0.1)
    print(f"Week: {weeks} | Savings: {savings}", end="\r", flush=True)

    savings += extra
    time.sleep(0.1)

    # if weeks % 52 == 0:
    #     savings = savings * intrest_rate


print(f"\nSavings: {savings}\nYou can retire")
print(f"\nIt took you {weeks} weeks ({round(weeks/52, 2)} years) to get to 2m")
