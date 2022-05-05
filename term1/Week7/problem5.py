# Siddhesh Zantye
# 23/03/2022

speed = int(input("How fast were you driving (km/h): ")) - 50
points = 0

if speed > 0:
    if speed < 11 and speed > 0:
        points = 10
    elif speed < 21 and speed > 10:
        points = 20
    elif speed < 31 and speed > 20:
        points = 35
    elif speed < 35 and speed > 30:
        points = 40
    else:
        points = 50

print(f"Points: {points}")
