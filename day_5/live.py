
# Password Simulation

password = "Milan123"
password_try_count = 5

print(f"Welcome to the password simulation. You have {password_try_count} tries to enter the correct password.")

while password_try_count > 0:
    user_input = input("Enter your password: ").strip()
    if user_input != password:
        password_try_count -= 1
        print(f"You entered wrong password. You have {password_try_count} tries left")
        if password_try_count == 0:
            print("You are out of tries")
    else:
        print("Correct Password")
        break


print("Simulation Complete")

