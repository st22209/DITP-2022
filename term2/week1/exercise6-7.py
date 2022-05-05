width = int(input("Enter width: "))

for i in range(width):
    print(" ".join([str((e+1)) for e in range((i+1))]) + " " * (width - i))

print()

for i in range(width, 0, -1):
    the_list = []
    for _ in range(i, 0, -1):
        the_list.append(str(_))

    print(" ".join(the_list))
