
# CLass variable
class Student:
    year = 2026
    num_of_students = 0

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Student.num_of_students += 1

student1 = Student("Ram", "ram@gmail.com")
print(Student.num_of_students)
student2 = Student("Hari", "hari@gmail.com")
print(Student.num_of_students)
student3 = Student("Shyam", "shyam@gmail.com")
print(Student.num_of_students)

print(f"The {Student.year} batch has {Student.num_of_students} Students")
print(f"Name: {student1.name} | Email: {student1.email}")
print(f"Name: {student2.name} | Email: {student2.email}")
print(f"Name: {student3.name} | Email: {student3.email}")



## Inheritance


# class Animal:  #Parent class
#     def __init__(self, name: str):
#         self.name = name
#         self.is_alive = True

#     def eat(self):
#         print(f"{self.name} is eating")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Prey(Animal):
#     def run(self):
#         print(f"{self.name} is running")

# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")


# class Rabbit(Prey):
#     pass

# class Hawk(Predator):
#     pass

# class Fish(Prey, Predator):
#     pass


# fish = Fish("Memo")

# fish.hunt()
# fish.run()


## Abstract class

# from abc import ABC, abstractmethod

# class Vehicle(ABC):

#     @abstractmethod
#     def go(self):
#         pass

#     @abstractmethod
#     def stop(self):
#         pass

# class MotorCycle(Vehicle):

#     def go(self):
#         print("Motorcycle is running")

#     def stop(self):
#         print("Motorcycle is Stopping")

# class Boat(Vehicle):

#     def go(self):
#         print("Boat is running")

#     def stop(self):
#         print("Boat is Stopping")


# motor = MotorCycle()

# boat = Boat()

# boat.go()
# boat.stop()

# motor.go()
# motor.stop()



## Super Function

# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled

#     def describe(self):
#         print(f"This shape is {self.color} and {"filled" if self.is_filled else "not filled"}")


# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius

#     def describe(self):
#         print(f"This is circle")
#         super().describe()
        

# class Square(Shape):
#      def __init__(self, color, is_filled, length):
#         super().__init__(color, is_filled)
#         self.length = length

# class Triangle(Shape):
#      def __init__(self, color, is_filled, base, height):
#         super().__init__(color, is_filled)
#         self.base = base
#         self.height = height
    



# c = Circle("red" , True, 7)
# s = Square(color= "green", is_filled=False, length=90)
# t = Triangle(color= "Blue", is_filled=False, base=30, height=20)

# c.describe()

# t.describe()



#Polymorphism


# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def add(self):
#         print(self.a + self.b)

# class B:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#     def add(self):
#         print(self.a + self.b + self.c)

# class C:
#     def __init__(self, a, b, c, d):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#     def add(self):
#         print(self.a + self.b + self.c +self.d)



# classes = [A(10,20), B(1,2,3), C(1,1,1,1)]

# for c in classes:
#     c.add()

