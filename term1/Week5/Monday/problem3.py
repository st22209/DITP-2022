prices = {
    "diesel" : 1.47,
    "91unleaded" : 2.06,
    "95octane" : 2.17
}

print("Initial Price: ")
x = print("\n".join([f"{k} = ${v}" for k, v in prices.items()]))

for k, v in prices.items():
    prices[k] = round(v*1.15, 2)

print("\nPrice Now: ")
x = print("\n".join([f"{k} = ${v}" for k, v in prices.items()]))

