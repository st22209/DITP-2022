def is_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    return False


number = int(input("Enter a number: "))
print(f"Number is {'prime' if is_prime(number) else 'not prime'}")
