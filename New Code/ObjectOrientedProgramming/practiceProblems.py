# 1. Create a Simple Class and Object
# Create a class Car with a method drive() that prints "Car is moving".
# Create an object of Car and call drive()

class Car:
    def drive(self):
        print("Car is Moving");


car1 = Car()
print(car1.drive())



# 2. Constructor and Attributes
# Create a class Person with a constructor (__init__) that accepts name and age as arguments and stores them as instance attributes.
# Create an object and print the person’s name and age.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def PrintPerson(self):
        return f"{self.name} and age is {self.age}"

Per1 = Person("Harry", 30)
print(Per1.name)
print(Per1.age)
print(Per1.PrintPerson())




# 3. Simple Inheritance
# Create a base class Animal with a method sound() that prints "Some sound".
# Create a derived class Dog that overrides sound() to print "Bark!".
# Create an object of Dog and call sound().

# class Animal:
#     def sound(self):
#         print("Some Sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# A1 = Animal()
# D1 = Dog()
# print(D1.sound())
# print(A1.sound())




