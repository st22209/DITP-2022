def get_grain(n):
    return 2 ** (n - 1)


for i in range(1, 65):
    print(f"Square: {i} | Grains: {get_grain(i)}")
