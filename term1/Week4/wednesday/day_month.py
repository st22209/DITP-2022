def day_month(day, month):
    day, month = day.upper(), month.upper()
    print(f"{day}\n{month}")

day = input("Day: ")
month = input("Month: ")

day_month(day, month)