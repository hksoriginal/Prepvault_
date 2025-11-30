OOPS_PY = '''
# OOPS in Python

Object-Oriented Programming (OOP) in Python is a programming paradigm that uses objects and classes. It helps to model real-world entities and allows reusability, encapsulation, and abstraction of code.

## Key Concepts

### 1. Class
A **class** is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods) of the object.

# Example: Class and Object
```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object of the class Dog
my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark()) #Output: Buddy says woof!
```


### 2. Object 
 An object is an instance of a class. When a class is defined, no memory is allocated until an object is created.

### 3. Inheritance 
 Inheritance allows a new class to inherit attributes and methods from an existing class. This promotes code reusability.

# Example: Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some sound"

class Dog(Animal): #Dog inherits from Animal
    def make_sound(self):
        return "Woof Woof!"

dog = Dog("Buddy")
print(dog.make_sound()) #Output: Woof Woof!

```
### 4. Encapsulation 
 Encapsulation restricts access to certain properties and methods from outside the class. This is done using private variables (with a leading underscore).

# Example: Encapsulation

```python
class Car:
    def __init__(self, make, model):
        self.__make = make  #Private variable
        self.__model = model

    def get_details(self):
        return f"Car: {self.__make} {self.__model}"

my_car = Car("Tesla", "Model S")
print(my_car.get_details()) #Output: Car: Tesla Model S
```
### 5. Polymorphism 
 Polymorphism allows methods to have the same name but behave differently based on the object calling it.

# Example: Polymorphism

```python

class Bird:
    def sound(self):
        return "Some bird sound"

class Sparrow(Bird):
    def sound(self):
        return "Chirp Chirp"

class Crow(Bird):
    def sound(self):
        return "Caw Caw"

birds = [Sparrow(), Crow()]

for bird in birds:
    print(bird.sound())
#Output:
#Chirp Chirp
#Caw Caw

```
### 6. Abstraction 
 Abstraction hides the internal implementation and shows only the necessary details.

# Example: Abstraction

``` python

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area()) #Output: 78.5
```


'''