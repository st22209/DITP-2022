password = "super_secret_password"

guesses = 3
guess_count = 0

while guess_count < 3:
    pswd = input("Enter the password: ")
    if pswd == password:
        print("Correct :)")
        break
    print("Wrong password :(")
    guess_count += 1
