code = int(input("Enter your secret number: "))

for i in range(9999):
    i = str(i)
    if len(i) != 4:
        i = f"{'0'*(4-len(i))}{i}"

    if int(i) == code:
        print(f"CODE FOUND: {i}")
        break