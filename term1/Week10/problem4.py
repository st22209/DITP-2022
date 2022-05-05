number = 0

user_num = int(input("Enter a number: "))

while number < user_num:
    number += 1
    if number % 2 == 0:
        print(number)
