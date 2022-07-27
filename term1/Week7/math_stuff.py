import numpy
from collections import Counter


def average(lst):
    return sum(lst) / len(lst)


def median(lst):
    n = len(lst)
    index = n // 2
    if n % 2:
        return sorted(lst)[index]
    return sum(sorted(lst)[index - 1 : index + 1]) / 2


def mode(lst):
    c = Counter(lst)
    return [k for k, v in c.items() if v == c.most_common(1)[0][1]]


def quartiles(lst):
    quartiles = numpy.quantile(lst, [0, 0.25, 0.5, 0.75, 1])
    quartiles = list(quartiles)

    new_data = {
        "Minimum": quartiles[0],
        "Maximum": quartiles[4],
        "LQ": quartiles[1],
        "UQ": quartiles[3],
    }

    return new_data


data = input("\nEnter data: ")
data = "".join([i for i in data.split()])
data = [int(i) for i in data.split(",")]

quartiles_list = quartiles(data)
data.sort()

print("\n\nResult:\n")
print(f"Ordered List: {', '.join([str(i) for i in data])}")
print(f"Median: {round(median(data), 2)}")
print(f"\nMean: {round(average(data), 2)}")
print(f"\nMode: {', '.join([str(i) for i in mode(data)])}\n")
print("\n\n".join([f"{key}: {value}" for key, value in quartiles_list.items()]))
print("\n\n")
