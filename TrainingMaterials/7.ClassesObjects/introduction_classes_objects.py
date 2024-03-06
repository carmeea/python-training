# CLASSES and OBJECTS in Python

"""
In Python, we use classes to create objects. 
A class is a tool, like a blueprint or a template, for creating objects. 
It allows us to bundle data and functionality together.

Real life example: A company that creates cars, needs a blueprint to produce a car. 
Based on this blueprint company can create as many cars as it wants
In Python the class is like the blueprint of the object, car. You can create as many objects as you want based on a class.
You also have car brands, car components, in python these are called attributes.

Class Syntax:
class ClassName:
    #Statements..

Objects consist of state, behavior, and identity. 
-Identity is the name of the object. Example: car
-Object has its unique state. We give each object its unique state by creating attributes in the __init__method of the class.
Example: Number of doors and seats in a car
-Behaviour of an object is what the object does with its attributes. We implement behavior by creating methods in the class.
Example: Accelerating and breaking in a car.

Object Syntax:
object_name = ClassName(*args)
"""


# Classes and Functions
class Vehicle:
    pass


print(Vehicle)

# Create an object car from the class Vehicle
car = Vehicle()  # object Instantiation


class Vehicle:
    wheels = 4  # Attribute


# Class attributes can also be accessed by class name rather than an object name
print("Vehicle wheels:", Vehicle.wheels)

car = Vehicle()
van = Vehicle()
print("Car wheels:", car.wheels)
print("Van wheels:", van.wheels)

# Changing Instance Attributes
car.wheels = 10  # changing instance attributes
print("Car wheels:", car.wheels)  # 10
print("Van wheels:", van.wheels)  # 4

# Changing Class attributes, will change the value in all objects of the class.
Vehicle.wheels = 5  # changing class attributes
print("Vehicle wheels:", Vehicle.wheels)
print("Car wheels:", car.wheels)
print("Van wheels:", van.wheels)


# __init__() method
"""
Similar to contructors in Java.Constructors are used to initializing the object state.
Constructor also contains a collection of statements(i.e. instructions) that are executed at the time of Object creation. 
It runs as soon as an object of a class is instantiated.
__init__() method is called as soon as we instantiate an object. 
The method helps to provide the state of the object. Using it, we can assign different values to different objects.

"""


class Vehicle:
    wheels = 4

    def __init__(self, doors):
        print(f"Object created with doors = {doors}")


car = Vehicle(2)  # Object created with doors = 2
van = Vehicle(6)  # Object created with doors = 6


# Self parameter in Python
"""
Almost all methods in the class have an extra parameter called self. It references the current object of the class.
the value of the self is provided automatically by Python. 
Instead of self, we can name it anything, as long as it is the first parameter of the method.
"""


# The self parameter it is used to reference the current object
class Vehicle:
    def __init__(self, type, brand):
        self.type = type
        self.brand = brand


vehicle1 = Vehicle("car", "Audi")  # instance attribute self.type=car, self.brand=Audi
vehicle2 = Vehicle("van", "Toyota")
print("Type:", vehicle1.type)
print("Brand:", vehicle2.brand)


class Vehicle:
    wheels = 4

    def __init__(self, name, doors, seats):
        self.name = name
        self.doors = doors
        self.seats = seats


vehicle1 = Vehicle("Car", 2, 2)
vehicle2 = Vehicle("van", 6, 12)
print("Vehicle1:", vehicle1.name, vehicle1.doors, vehicle1.seats)
print("Vehicle2:", vehicle2.name, vehicle2.doors, vehicle2.seats)


# Restricting Access to Attributes

# Double underscore restricts access to the attribute name. Error raised is AttributeError.
# It applies to both class attributes and instance attributes.


class Vehicle:
    __name = "Car"
    brand = "Audi"


print("Vehicle class Brand =", Vehicle.brand)
# print(Vehicle.__name)  # AttributeError: type object 'Vehicle' has no attribute '__name'


# Methods in classes


class Vehicle:
    wheels = 4

    def __init__(self, name, doors, seats):
        self.name = name
        self.doors = doors
        self.seats = seats

    def accelerate(self, distance):
        return f"{self.name} has travelled {distance} Miles."


car = Vehicle("Car", 2, 2)
print(car.accelerate(10))


# INHERITANCE
# Syntax: class SubClass(SuperClass):


class ParentClass:  # Superclass
    def parent_method(self):
        return "ParentClass method"


class ChildClass(ParentClass):  # Subclass
    def child_method(self):
        return "ChildClass method"


parent = ParentClass()
print("parent:", parent.parent_method())
child = ChildClass()
print("child:", child.child_method())
print("child:", child.parent_method())

# issubclass() - built-in function. Used to find whether a class is a subclass or not. It returns True or False
print("ChildClass is subclass of ParentClass:", issubclass(ChildClass, ParentClass))
print("ParentClass is subclass of ChildClass:", issubclass(ParentClass, ChildClass))


# POLYMORPHISM
"""
Using the same block of code (in different classes) to accomplish different objectives is called polymorphism.
"""


class Solomon:
    def __init__(self):
        self.name = "Solomon"
        self.age = 50

    def get_name(self):
        print(f"Hello, my name is {self.name}.")

    def get_age(self):
        print(f"I am {self.age} years old.")


class Charles:
    def __init__(self):
        self.name = "Chales"
        self.age = 20

    def get_name(self):
        print(f"Hey! I am {self.name}.")

    def get_age(self):
        print(f"I am {self.age} years old.")


person1 = Charles()
person2 = Solomon()
for person in (person1, person2):
    person.get_name()
    person.get_age()


# ABSTRACT CLASS
""""
Abstract class is a template for other classes or base class
Like the name suggests, it is only abstract and can not be instantiated. 
A class should contain at least one abstract method to become an abstract class.
From the abc module, we need to import ABC class to inherit and abstract method decorator to create abstract methods. 
abc module=abstract base class module
Abstract classes can have a normal method and an abstract method
"""

from abc import ABC, abstractmethod


# abstract class
class Employee(ABC):
    @abstractmethod
    def sector(self):
        pass


class GovtEmployee(Employee):
    # Overriding abstract method
    def sector(self):
        print("I work in Government sector")


class PrivateEmployee(Employee):
    # Overriding abstract method
    def sector(self):
        print("I work in Private sector")


emp1 = GovtEmployee()
emp2 = PrivateEmployee()
emp1.sector()
emp2.sector()
# emp = Employee()  # TypeError: Can't instantiate abstract class Employee ...


# Built-in Functions for Attributes
# getattr()
class Vehicle:
    color = "Blue"
    wheels = 4


car = Vehicle()
print(getattr(car, "color"))  # Blue

# hasattr()
print(hasattr(car, "color"))  # True

# setattr()
# used to set an attribute. If the given attribute does not exist, then it would be created.
print("Color before", car.color)
setattr(car, "color", "Red")  # Changing an existing attribute
print("Color after changing", car.color)
setattr(car, "speed", 120)  # Creating a new attribute for car instance only
print("New attribute car speed:", car.speed)
# print(Vehicle.speed)  # 'Vehicle' has no attribute 'speed'

# delattr()
delattr(Vehicle, "color")
# print(Vehicle.color)  # 'Vehicle' has no attribute 'color'


# del Keyword
"""
del keyword can be used to delete classes, objects and its attributes. 
If we try to access a deleted class or object, it raises a NameError 
if we try to access a deleted attribute, it raises an AttributeError.
Syntax: del object_name
"""


class MyClass:
    name = "something"


print("Before Deleting", MyClass)
del MyClass
try:
    print(MyClass)
except NameError:
    print("Class Deleted")


# delete an Attribute using del
class MyClass:
    name = "class"
    name2 = "something"


print("Before Deleting An Attribute = ", MyClass.name2)
del MyClass.name2
try:
    print(MyClass.name2)
except AttributeError:
    print("Attribute Deleted")


# Built-in Attributes
# __dict__ - contains the dictionary containing the class’s namespace
class Vehicle:
    pass


print(Vehicle.__dict__)

# __name__ - contains the class name
print("Class name:", Vehicle.__name__)

# __module__ - contains the name of the module in which the class is defined.
# The attribute is “__main__” in interactive mode.
print("Vehicle module:", Vehicle.__module__)

# __bases__ - contains the tuple containing the class’s base classes.
print("Base class:", Vehicle.__bases__)


# __doc__ - contains a string of the documentation of the class. It is None if no documentation is defined.
print(Vehicle.__doc__)


class Cars:
    """Demonstrate docstring"""


print("Documentation:", Cars.__doc__)
