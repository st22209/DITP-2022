password = "super_secret_password"

while True:
    pswd = input("Enter the password: ")
    if pswd == password:
        print("Correct :)")
        break
    print("Wrong password :(")
