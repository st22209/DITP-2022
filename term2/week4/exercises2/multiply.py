def multiply_list(numbers: list[int], multiply: int = 5) -> list[int]:
    return [i * multiply for i in numbers]


the_list = [1, 4, 2, 5, 11, 5, 6, 2]

print(multiply_list(the_list))
print(multiply_list(the_list, 2))  # passing the arg
