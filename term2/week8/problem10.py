def printlabel(size):
    print(" ______________________ ")
    print("|Dresswell Clothing Co |")
    print(" ******size " + str(size) + " *****")
    print("|______________________|")


sizes = [6, 8, 10, 12, 14, 16, 18, 20]

for size in sizes:
    for i in range(size):
        for i in range(100):
            printlabel(size)
