number = 0

user_num = int(input("Enter a number: "))
multiple = int(input("Enter the multiple: "))

while number < user_num:
    number += 1
    if number % multiple == 0:
        print(number)
