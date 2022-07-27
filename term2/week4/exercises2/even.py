def get_even(numbers: list[int]) -> list[int]:
    return [i for i in numbers if i % 2 == 0]


print(get_even([1, 2, 3, 4, 5, 6, 7, 8, 9]))
