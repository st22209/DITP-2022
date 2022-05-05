# Siddhesh Zantye
# 23/03/2022

age = int(input("What is your age: "))
learners = int(input("How many months have you held onto you drivers licence? "))


if age >= 17 and learners >= 6:
    print("You can apply for you restricted licence YAY :)")

if age >= 17 and learners < 6:
    print(f"You cant apply now but if you hold your licence for {6-learners} more months\nYou can get your licence then")

if age < 17:
    print(f"You cant apply till you're 17 ({17-age} more years)")