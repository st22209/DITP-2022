total = 0

holes = int(input("How many holes does this game have? "))

for i in range(holes):
    total += int(input(f"Enter score for hole {i+1}: "))

print("Sum:", total)