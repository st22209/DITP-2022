# Siddhesh Zantye
# 23/03/2022

exam = int(input("What did you get on your exam? "))

if exam == 0:
    print("You were absent")
elif exam < 50:
    print("You failed mate get good")
elif exam < 65:
    print("You got achieved")
elif exam < 85:
    print("You got merit")
elif exam >= 85:
    print("You got Excellence")
