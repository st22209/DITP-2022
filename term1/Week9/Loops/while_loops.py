# count = 1
# while count < 5:
#     print(count)
#     count += 1

# number = int(
#     input(
#         "Enter any number between 100 and 500 "
#     ))
# while number < 100 or number > 500:
#     print(
#         "Incorrect number, \
#     Please enter correct number"
#     )
#     number = int(input("Enter a Number between 100 and 500 "))
# else:
#     print("Given Number is correct", number)


# n = int(
#     input("Please Enter Number ")
# )
# while n > 0:
#     if n % 2 == 0:
#         print(n, "is a even number")
#     else:
#         print(n, "is a odd number")
#     n -= 1

# name = "Jesaa29Roy"
# size = len(name)
# i = 0
# while i < size:
#     if name[i].isdecimal():
#         break
#     print(name[i], end=" ")
#     i = i + 1


# numbers = [2, 3, 11, 7]
# for i in numbers:
#     print("Current Number is", i)
#     if i > 10:
#         continue
#     square = i * i
#     print("Square of a current number \
#         is", square)


# name = "Je sa a"
# name_no_space, space_count = "", 0

# size = len(name)
# i = -1
# while i < size - 1:
#     i = i + 1
#     if name[i].isspace():
#         space_count += 1
#         continue
#     name_no_space += name[i]

# print(
#     f"Removed {space_count} spaces\nName: \
# {name_no_space}"
# )


# for i in range(1, 11):
#     print('Multiplication table of', i)
#     for j in range(1, 11):
#         if j == 5: continue
#         print(i * j, end=' ')
#     print('')


# for i in range(1, 11):
#     if i % 2 == 0: continue
#     print('Multiplication table of', i)
#     for j in range(1, 11):
#         print(i * j, end=' ')
#     print('')

# months = ["January", "June", 
#     "March", "April"]
# for mon in months:
#     pass
# print(", ".join(months))
