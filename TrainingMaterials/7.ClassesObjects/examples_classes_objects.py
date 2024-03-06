"""
1.Create an empty class and an object for the class without raising an error.
"""


class DoesNothing:
    pass


obj = DoesNothing()


"""
2.Create a class named Square and initialize it with length. Create two methods to return perimeter and area.
"""


class Square:
    def __init__(self, length):
        self.length = length

    def getPerimeter(self):
        return round(4 * self.length)

    def getArea(self):
        return round(self.length * self.length)


square1 = Square(3)
print("Perimeter: ", square1.getPerimeter())
print("Area:", square1.getArea())

"""
3.Create a class named Employee and initialize with name and id. 
Create a common attribute for all objects named retirement_age with a value of 50. 
Also create methods:
years_to_work() - Returns how many years an employee has to work until retirement from his current age.
setSalary() - Assign salary to the employee
getSalary() - Returns salary of the employee
"""


class Employee:
    retirement_age = 50

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.salary = None
        self.remaining_years = None

    def years_to_work(self, present_age):
        self.remaining_years = self.retirement_age - present_age
        return self.remaining_years

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary


employee1 = Employee("Ion", "1")
employee1.setSalary(2000)
print("Employee id:", employee1.id)
print("Employee name:", employee1.name)
print("Years remaining: ", employee1.years_to_work(31))
print("Salary:", employee1.getSalary())

"""
4.What is the output of the following code?
"""


class Person:
    """Basic template of Person"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return f"{self.name} is Eating"

    def birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old."


jack = Person("Jack", 2)
print(jack.__doc__)
print(jack.eat())
print(jack.birthday())

# Answer:
# Basic template of Person
# Jack is Eating
# Jack is now 3 years old.

"""
5.A few weeks ago, Sam created a class named Fruit and sent the file to his friend. 
His friend came across a bug and informed Sam about it.
 After spending hours thinking, he is now sure that the bug is being caused by a certain attribute in the class. 
 He is not sure whether it is being caused because of its presence or absence. 
 Since he can not directly edit the file, he decided to send his friend another file that modifies the already existing class. 
 He wants to delete the attribute lemons if it exists or if it doesn't exist, then he wants to create it with value 24. 
 Help Sam finish the code.
"""


class Fruit:
    carrots = "Red Carrots"
    # lemons = "Green Lemons"


print("Fruit has attribute lemons:", hasattr(Fruit, "lemons"))
if hasattr(Fruit, "lemons"):
    delattr(Fruit, "lemons")
else:
    setattr(Fruit, "lemons", 24)
print("Lemons:", Fruit.lemons)
