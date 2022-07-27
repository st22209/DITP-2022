"""
Problem 1:
The number 353 in the numbers list has been determined to be an error. It
should have been 53. Find this value and replace it, then display the
contents of the list to prove that it has been changed. (You cannot use a for
number in numbers style of loop for this solution, as you will need to know
the index of the integer to be replaced)
Algorithm
1. start at first element
2. loop until replacement made or end of data
○ 2.1 check whether element matches 353
○ 2.2 if a match, change it to 53
○ 2.3 next element
"""

numbers_list = [65, 21, 9, 84, 67, 353, 10, 26, 7, 25, 66, 94, 20, 38]

print(f"Before: {numbers_list}")

index = 0
while index < len(numbers_list):
    value = numbers_list[index]
    if value == 353:
        numbers_list[index] = 53
        break
    index += 1
else:
    print("353 was not found in this list")

print(f"After: {numbers_list}")
