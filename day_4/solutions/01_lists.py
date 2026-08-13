# ---------------------------------------------------------
# SOLUTION 1: LISTS — Storing Many Values 📝
# ---------------------------------------------------------


# TASK 1
movies = ["Inception", "Spirited Away", "The Matrix"]
print(movies)
print(movies[0])


# TASK 2
movies[1] = "Interstellar"
movies.append("Avengers")
movies.insert(0, "Toy Story")
print(movies)


# TASK 3
removed = movies.pop()
print("Removed:", removed)
movies.sort()
print("Sorted:", movies)
print("Length:", len(movies))


# TASK 4
numbers = [4, 2, 8, 2, 9, 2]
print("Count of 2:", numbers.count(2))
print("Index of 8:", numbers.index(8))
numbers.reverse()
print("Reversed:", numbers)


# BONUS CHALLENGE
fruit = input("Enter a fruit: ")
fruits = ["apple", "banana", "cherry", "mango"]
if fruit in fruits:
    print(fruit, "is in the basket!")
else:
    print(fruit, "is not in the basket.")
