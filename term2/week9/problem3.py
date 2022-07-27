# Design and write a program which gets data for a list of float values from
# the user, then multiplies every element in the list by 3, overwriting the old
# values with the new values. Use a for loop to display all the values in the
# list twice, once before and once after the multiplication.

floats = []

try:
    floats: list = [
        float(i)
        for i in list(
            input("Enter your numbers separated by a comma (eg 1.7, 2, 5.3, 2): ")
            .replace(" ", "")
            .strip()
            .split(",")
        )
    ]
except ValueError:
    print("ENTER NUMBERS MAN")

print(floats)

for idx, i in enumerate(floats):
    floats[idx] = i * 3

print(floats)
