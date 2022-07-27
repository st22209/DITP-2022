amount = int(input("How many numbers will you be giving: "))

numbers = []

for i in range(amount):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

print(f"Total is {sum(numbers)}\nAverage is {round((sum(numbers) / len(numbers)), 2)}")
