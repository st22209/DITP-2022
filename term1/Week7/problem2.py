# Siddhesh Zantye
# 23/03/2022

temp = input("What is your temperature? ")
age = input("What is your age? ")

print(f"temperature: {temp}\n\nage: {age}")

try:
    temp = int(temp)
    age = int(age)
except ValueError:
    print("Age and temperature must be an int")

if age < 3 and temp > 38:
    print("Call a doctor")
if age > 3 and temp > 39.5:
    print("High fever")
else:
    print("Your temperature is okay, check again in an hour.")
