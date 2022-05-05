# Siddhesh Zantye
# 23/03/2022

home = int(input("How much did the home team score"))
visitor = int(input("How much did the visiting team score"))

if home > visitor:
    print("The home team won")
elif visitor > home:
    print("The vistor team won")
else:  
    print("it was a draw")