# Siddhesh Zantye
# 23/03/2022

# 8

age = int(input("What is your age? "))
credits = int(input("How many NCEA Level 3 credits do you have? "))

if age >= 18 and credits >= 60:
    print("You can apply")

elif age < 18 and credits >= 60:
    print("You can apply for restricted entry")

else:
    print("You can apply")

# 8b

def apply(credits : int, age : int) -> None:
    if age >= 20:
        print("You can apply")
    elif age >= 16 and credits >= 60:
        print("You can apply with restricted entry")

age = int(input("What is your age? "))
credits = int(input("How many NCEA Level 3 credits do you have? "))

apply(credits, age)