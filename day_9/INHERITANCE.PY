#-----------------------------------------
#Homework: defult parameters
#-----------------------------------------

#Task 1: Greeting wwith defult 

def welcome(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(welcome("Sam"))
print(welcome("Sam, Hi"))
print(welcome("Sam", "Goodmorning "))

# Tak 2: Power function 

def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 3))
print(power(5, 0))

#Task 3: order summary

def order_summary(iteam_name,
quantity=1, price_each=10.0):
    total = quantity * price_each
    return f"{quantity} * {iteam_name} = ${total}"

print(order_summary("pencil"))
print(order_summary("notebook", 3))
print(order_summary("pen, 5, 2.5"))

#Task 4: Safe divider

def safe_divide(numerator,
denominator=1):
    if denominator ==0:
     return "Cannot divide by zero!" 
    return numerator / denominator

print(safe_divide(10, 2))
print(safe_divide(5, 0))
print(safe_divide(7))

# Bonus challange

def create_profile(username, 
status="active", role="user"):
    return{
        "username": username,
        "status": status,
        "role": role
    }

print(create_profile("john"))
print(create_profile("alice",
 "offline"))
print(create_profile("bob", "active", 
"admin"))
