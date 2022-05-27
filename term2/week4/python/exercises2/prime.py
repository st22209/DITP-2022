def is_prime(num: int) -> bool:
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    return False

print(is_prime(5))
print(is_prime(20))