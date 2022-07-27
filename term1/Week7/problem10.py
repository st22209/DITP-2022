# Siddhesh Zantye
# 23/03/2022

accounts = {
    "Oliver": {"username": "user1", "password": "password", "level": 3},
    "Charlotte": {"username": "user2", "password": "password", "level": 5},
    "William": {"username": "user3", "password": "password", "level": 2},
    "Ava": {"username": "user4", "password": "password", "level": 1},
}


while True:
    found = False
    name = input("What is your name: ")

    for key, value in accounts.items():
        if key.lower() == name.lower():
            found = True
            print(f"\nWelcome {name}, Your details are bellow:\n")

            print("\n".join([f"{k} : {v}" for k, v in value.items()]), end="\n\n")
            break

    if not found:
        print("User with that name does not exist")
    else:
        break
