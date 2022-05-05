import time

start_temp = 115
perfect_temp = 112

while start_temp > perfect_temp:
    start_temp -= 0.1
    print("temperature:", round(start_temp), end="\r")
    time.sleep(0.1)

print("\nTea is ready")