# 5A:

prices = [12.5, 6, 3.55]
total = 0

def add_total(x):
    global total
    total += x

x = [add_total(i*2) for i in prices]

print(f"5a:\nTotal Price: ${total}\n")

# 5B:

prices = [12.5, 6, 3.55]
total = 0

for i in prices:
    if i == 3.55:
        total += (i*4)
    else:
        total += (i*2)


print(f"5b:\nTotal Price: ${total}")