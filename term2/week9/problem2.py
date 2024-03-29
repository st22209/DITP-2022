# Write a program which finds the largest element in a list of float values. The
# algorithm suggests a solution. (Use the numbers list from the previous
# examples to test the implementation of the algorithm).
# Algorithm
# 1. first element is the largest
# 2. loop until end of data
# 2.1 if element is larger than largest
# 2.1.1 largest = this element
# 2.2 next element

numbers_list = [
    65,
    21,
    9,
    84,
    67,
    35,
    10,
    26,
    7,
    25,
    66,
    94,
    20,
    38,
    19,
    79,
    61,
    54,
    64,
    82,
    89,
    59,
    63,
    43,
    29,
    3,
    71,
    28,
    99,
    81,
    72,
    41,
    68,
    50,
    58,
    35,
    87,
    85,
    93,
    47,
    17,
    39,
    44,
    77,
    55,
    18,
    70,
    37,
    75,
    49,
    11,
    60,
    4,
    24,
    36,
    40,
    23,
    86,
    15,
    32,
    31,
    48,
    34,
    13,
    46,
    12,
    8,
    2,
    14,
    57,
    56,
    6,
    42,
    45,
    51,
    16,
    76,
    53,
    80,
    83,
    22,
    91,
    90,
    98,
    62,
    73,
    52,
    88,
    96,
    69,
    78,
    5,
    92,
    30,
    95,
    97,
    1,
    33,
    74,
]

largest_value, index = numbers_list[0], None

for idx, i in enumerate(numbers_list):
    if i > largest_value:
        largest_value = i
        index = idx

print(
    f"{numbers_list}\nThe largest value was {largest_value} and the index of that is {index}"
)
