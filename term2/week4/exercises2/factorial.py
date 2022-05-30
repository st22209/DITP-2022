def factorial(n: int) -> int:
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


print(factorial(5))

# or 

range_list = (list(reversed(range(1, 5))))

total = 5
for i in range_list:
    total = i*total

print(total)