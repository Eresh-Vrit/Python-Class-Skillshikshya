# ---------------------------------------------------------
# SOLUTION 4: WHILE LOOP 🔁
# ---------------------------------------------------------
import random


# TASK 1: Rocket Countdown.
start = int(input("Countdown from: "))
while start > 0:
    print(f"T minus {start}...")
    start -= 1
print("Liftoff! BLAST OFF!")


# TASK 2: Password Retry.
secret = "python"
guess = input("Password: ")
while guess != secret:
    print("Wrong! Try again.")
    guess = input("Password: ")
print("Access granted! (unlocked)")


# TASK 3: Simple Calculator with a flag.
running = True
while running:
    entry = input("Number (or 'quit'): ")
    if entry == "quit":
        running = False
    else:
        n = float(entry)
        print(f"Square: {n}^2 = {n}")
print("Bye!")


# ⭐ BONUS CHALLENGE: Multiplication quiz (5 questions, 2 attempts each).
score = 0
for q in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    correct = a * b
    for attempt in range(2):
        try:
            answer = int(input(f"What is {a} x {b}? "))
        except ValueError:
            print("Please enter a number.")
            continue
        if answer == correct:
            print("Correct!")
            score += 1
            break
        else:
            if attempt == 0:
                print("Wrong -- try once more.")
            else:
                print(f"Out of attempts. Answer was {correct}.")
print(f"\nFinal score: {score}/5")
