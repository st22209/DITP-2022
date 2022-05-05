def isprime(num):
    if num > 1:  
        for n in range(2,num):  
            if (num % n) == 0:  
                return False
        return True
    else:
        return False

for i in range(25, 51):
    if isprime(i):
        print(i)
