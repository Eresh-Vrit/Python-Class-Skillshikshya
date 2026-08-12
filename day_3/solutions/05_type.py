# ---------------------------------------------------------
# SOLUTION 5: type() 🔍
# ---------------------------------------------------------


# TASK 1: type() Detective
my_string = "hello"
my_int = 42
my_float = 3.14
my_bool = True

print(f"Value: {my_string}    Type: {type(my_string)}")
print(f"Value: {my_int}       Type: {type(my_int)}")
print(f"Value: {my_float}     Type: {type(my_float)}")
print(f"Value: {my_bool}      Type: {type(my_bool)}")


# TASK 2: Type Conversion
num_text = "50"
pi_text = "3.14"
age_text = "15"

print(int(num_text))              # 50
print(float(pi_text))             # 3.14
print(f"Next year: {int(age_text) + 1}")   # 16


# TASK 3: input() Trap
birth_year = input("What year were you born? ")
print(f"Type before conversion: {type(birth_year)}")
age = 2024 - int(birth_year)
print(f"You are approximately {age} years old!")


# TASK 4: str() Conversion
year = 2024
print("The current year is " + str(year))


# ⭐ BONUS CHALLENGE:
price = float(input("Enter a price: "))
final_price = round(price * 1.10, 2)
print(f"Final price: Rs. {final_price}")
