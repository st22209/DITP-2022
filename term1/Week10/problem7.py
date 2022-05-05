numbers_count = int(input("How many numbers do you have? "))
numbers_list = []
i = 0
while i < numbers_count:
    try:
        num = int(input("Enter the number: "))
    except Exception:
        print("ERROR\nMost likely because the number entered was not int")
        continue
    numbers_list.append(num)
    i += 1

print(
    f"Numbers: {', '.join((str(i) for i in numbers_list))}\n\
Sum: {sum(numbers_list)}\nAverage: {sum(numbers_list)/len(numbers_list)}"
)
