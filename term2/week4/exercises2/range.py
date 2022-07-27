def in_range(n: int, range: int, start: int = 0) -> bool:
    if n >= start and n <= range:
        return True
    return False


print(in_range(5, 10))
print(in_range(12, 34, 52))
