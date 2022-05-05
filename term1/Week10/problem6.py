num1, num2, num3 = None, None, None

while True:
    num1, num2, num3 = None, None, None

    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        num3 = int(input("Enter the third number: "))
    except Exception:
        print("ERROR\nMost likely because the number entered was not int")
        continue

    if num1 is not None and num2 is not None and num3 is not None:
        break

print((num1 + num2 + num3) / 3)
