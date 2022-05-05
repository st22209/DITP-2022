# Siddhesh Zantye
# 23/03/2022

have_you_been = input("Have you been in uk in 1985 (y/n): ")
try:
    age = int(input("What is your age: "))
    weight = int(input("What is your weight? "))
except ValueError:
    print("You must enter a number")

if have_you_been.lower() in ['yes', 'y']:
    print("You cannot give blood")
    quit()

if age > 16 and weight > 50:
    print("You can give blood")
else:
    print("You cannot give blood")  