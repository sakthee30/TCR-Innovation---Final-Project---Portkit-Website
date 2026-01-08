#classes
class Point:

    #methods
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point1 = Point()
#attributes
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
print(point2.x) #this results in error saying [Point object has no attribut]

#To fix the above solution, will use CONSTRUCTORS
#A constructor is a function that gets called at the time of creating an object.

class Point:
    #constructor
    #this method is used to construct or create a object
    def __init__(self,x,y): 
        self.x = x
        self.y = y

    #methods
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point = Point(10,20) #to add these coordinates, will should add constructor at the top
print(point.x)
#whenever we create a new point object, self references that object in memory, the same object that we are referencing using this variable

#TASK
class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
        return f"Hi I'm {self.name}"

person_name = Person('Sakthee')
person_name.talk()

bob = Person("Jaisurya")
bob.talk()

#OOPS in python
#1.Inheritance
#let's say we have two classes DOG and CAT, and if we want to pass the same statements inside these two classes, whenever if there is any mistake, it affects both the classes;instead we can create a inheritant class and inherits the features to other classes

class Mammal:
    def walk(self):
        print("Walk")
class Dog(Mammal):
    def barking(self):
        print("Barking")
class Cat(Mammal):
    #since there is not statements to execute; we should declare pass, pass means do nothing
    pass

dog1 = Dog()
dog1.barking()
dog1.walk()
#both dog and cat classes are inheriting the classes defined in parent class(Mammal)

#2.polymorphism
#Function polymorphism
class Dog:
    def sound(self):
        return "Bark"
class Cat:
    def sound(self):
        return("Meow")

def make_sound(animal):
    print(animal.sound())

make_sound(Dog())
make_sound(Cat())

#operator overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


#if we try to access objects
p1 = Point(2,3)
p2 = Point(4,5)

p3 = p1 + p2
print(p3)

#Polymorphism
#2types -> Method overloading[python does not have] & Method overriding

#Method Overriding
#Same methods with same number of arguments/parameters but with different class
class A:
    def show(self):
        print("in A show")
class B(A):
    def show(self):
        print("in B show")

#this prints only the method in B (because its overrides)
a1 = B()
a1.show()

#3.Abstraction ABC --> abstract base classes
from abc import ABC, abstractmethod

class Vehicle(ABC):

#if i dont want any developer to use this vehicle class, will define it as abstract class [ABC] and can also add abstract methods; 
# these methods will be inherited by its children
#to use abstractmethod we need to use decorator [@abstractmethod]

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

#prevents instantiation of class iteself; this results in error [Can't instantiate abstract class vechicle with abstract methods go, stop]
vehicle = Vehicle()

#Instead we will create some children to inherit from this class

class Car(Vehicle):

    #without passing any methods in this child class; we will receive a warning saying that class Car must implement all abstract methods;
    #so if we put pass here; it will results in same error; we need to implement abstract methods in abstract class

    def go(self):
        print("You drive the car")
    
    def stop(self):
        print("You stop the car")

car = Car()
car.go()
car.stop()
#this works perfectly

#creating another child class
class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")
    
    #If we try to implement only go method in child class without implementing stop method
    # this will also result in same type error saying  [Can't instantiate abstract class motorcycle with abstract methods go, stop]

    def stop(self):
        print("You stop the motorcycle")

motorcycle = Motorcycle()
motorcycle.go()
motorcycle.stop()

#Encapsulation
#example 1
class Computer():

    def __init__(self):
        self.__maxprice = 900 #private

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice)) #getter

    def setMaxPrice(self, price):
        self.__maxprice = price #setter

comp1 = Computer()
comp1.sell()
comp1.__maxprice = 1000 #still 900 will be printed; since it is a private variable and still not updated
comp1.sell()
comp1.setMaxPrice(2000) # calling after updation
comp1.sell()

#example 2
class Car:
    def __init__(self, brand, speed):
        self.nrand = brand  #public
        self.__speed = speed #private

    def get_speed(self):
        return self.__speed #getter
    
    def set_speed(self, speed):
        if speed > 0:
            self.__speed = speed    #setter
        else:
            print("Invalid speed")

c = Car("BMW",120)
print(c.brand) #accessing public data
print(c.__speed) #accessing private (results in error)

#access using getter
print(c.get_speed) #prints 120
        
