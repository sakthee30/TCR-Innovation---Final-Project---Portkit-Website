#TASK
#1.create a student class
#attributes -> name, roll_no, marks_list
#methods -> add_mark(), calculate_average()

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks = []

    def add_mark(self, mark):
        if mark >= 0 and mark <=100:
            self.marks.append(mark)
            print(f"Marks {mark} added successfully")
        else:
            print("Invalid")
    
    '''
    #to get marks from user
    def get_marks(self):
        print("Enter marks for 5 subject: ")
        for i in range(1,6):
            mark = int(input("Enter mark for subject {i} : "))
            if mark >= 0 and mark <=100:
                self.marks.append(mark)
            else:
                print("Invalid")
    '''
    
    def cal_avg(self):
        if(len(self.marks) == 0):
            return 0
        total = sum(self.marks)
        average = total / len(self.marks)
        return average
    
    def display_details(self):
        print("Student name: ", self.name)
        print("Roll number: ", self.roll_no)
        print("Marks: ", self.marks)
        print("Average: ", self.cal_avg())


student1 = Student("Sakthee", 57)
student1.add_mark(90)
student1.add_mark(80)

student1.display_details()

#2.create class bankaccount
#attributes -> account holder, balance
#methods -> deposit, withdraw, check balance

class Bank_Account:
    def __init__(self, acc_holder, balance):
        self.acc_holder = acc_holder
        self.balance = balance 
    
    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Amount {amount} added successfully")
        else:
            print("Invalid")

    def withdraw(self, amount):
        if amount > 0:
            if amount < self.balance:
                self.balance = self.balance - amount
            else:
                print("Insufficient Balance")
    
    def check_balance(self):
        return self.balance
    
result = Bank_Account("Sakthee", 25000)
result.deposit(5000)
result.withdraw(2000)
result.check_balance()

#3.Calculator
#create class calc
#methods -> add, sub, mul, div

class Calc():
    def __init__(self):
        pass

    def add(self, num1, num2):
        sum = num1 + num2
        print(f"The sum of {num1} and {num2} is {sum}")
        return sum
    
    def sub(self, num1, num2):
        sub = num1 - num2
        print(f"The subtraction of {num1} and {num2} is {sub}")
        return sub
    
    def mul(self, num1, num2):
        mul =  num1 * num2 
        print(f"The multiplication of {num1} and {num2} is {mul}")
        return mul
    
    def div(self, num1, num2):
        div = num1 / num2
        print(f"The Division of {num1} and {num2} is {div}")
        return div

result = Calc()
result.add(10,20)
result.sub(10,20)
result.mul(10,20)
result.div(10,20)

#INHERITANCE 
#TASK on single level inheritance
#TASK 1
#vehicle -> car
#base class -> Vehicle(attributes:brand, model)
#derived class -> car(attribute: fule_type)
#create objects of car and print full details using a method

class Vehicle():
    #constructor
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 
        
    def vehicle_info(self):
        print(f"The brand is {self.brand}")
        print(f"The model is {self.model}")

class Car(Vehicle):
    #call the parent constructor
    def __init__(self, brand, model, fuel_type): 
        super().__init__(brand, model)
        self.fuel_type = fuel_type

#super() is used in inheritance to call methods of the parent class without mentioning the parent class name
#in simple, super() gives access to the parent class

    def car_info(self):
        self.vehicle_info() #calling parent method
        print(f"The fuel type is {self.fuel_type}")

my_car = Car("Toyota", "Tata", "Diesel")
my_car.car_info()

#TASK 2
#Animal -> Dog
#Animal:species Dog:breed, sound
#add a method make_sound() that print the dog's sound

class Animal():
    def __init__(self,species):
        self.species = species

    def show_species(self):
        print(f"The species is {self.species}")

class Dog(Animal):
    def __init__(self, species, breed, sound):
        #calling the parent constructor
        super().__init__(species)
        self.breed = breed
        self.sound = sound

    def show_dog_info(self):
        self.show_species() #calling parent method
        print(f"The breed is {self.breed}")
        print(f"The sound is {self.sound}")

my_dog = Dog("Mammal", "Doberman", "Bow-Bow")
my_dog.show_dog_info()

#TASK 3
#Base class -> Person -> Attributes -> name, age
#method -> show_person() -> prints name and age
#derived class -> employee -> Attributes -> employee id, salary
#method -> show_emp() -> call show_person() from parent -> print emp_id, sal

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def show_person(self):
        print(f"The name is {self.name}")
        print(f"The age is {self.age}")

class Employee(Person):
    def __init__(self,name,age,id,salary):
        super().__init__(name,age)
        self.id = id
        self.salary = salary

    def show_emp(self):
        self.show_person()
        print(f"The employe id is {self.id}")
        print(f"The salary is {self.salary}")

result = Employee("Sakthee",24,57,25000)
result.show_emp()

#TASK on multi level inheritance
#TASK 1
#Person -> attributes name, age
#student -> attributes roll_no, marks
#clgstudent -> attributes dept, year

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def person(self):
        print(f"The name of the person is {self.name}")        
        print(f"The age is {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no, marks):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.marks = marks
    
    def student(self):
        print(f"The roll_no is {self.roll_no}")
        print(f"The marks is {self.marks}")

class Clgstudent(Student):
    def __init__(self, name, age, roll_no, marks, dept, year):
        super().__init__(name, age, roll_no, marks)
        self.dept = dept
        self.year = year

    def details(self):
        self.person()
        self.student()
        print(f"The department is {self.dept}")
        print(f"The year is {self.year}")

result = Clgstudent("Sakthee",23,57,95,'AI',2024)
result.details()

#TASK 2
#Electronics -> attributes : brand
#phone -> attributes : battery
#smartphone -> attributes RAM, storage

class Electronics():
    def __init__(self,brand):
        self.brand = brand
    
    def ph_brand(self):
        print(f"The brand is {self.brand}")

class Phone(Electronics):
    def __init__(self, brand, battery):
        super().__init__(brand)
        self.battery = battery

    def ph_details(self):
        print(f"The battery is {self.battery}")

class Smartph(Phone):
    def __init__(self,brand,battery,ram,storage):
        super().__init__(brand,battery)
        self.ram = ram
        self.storage = storage

    def smt_details(self):
        self.ph_brand()
        self.ph_details()
        print(f"The RAM is {self.ram}")
        print(f"The storage is {self.storage}")

details = Smartph("Oneplus",1600,8,128)
details.smt_details()

#TASK on multiple inheritance
#TASK 1
#Teacher -> teaches_subject
#Researcher -> research_field
#Professor inherits both

class Teacher():
    def __init__(self,name,subject):
        self.name = name
        self.subject = subject
    
    def teaches(self):
        print(f"The name of the teacher is {self.name}")
        print(f"The subject is {self.subject}")

class Researcher():
    def __init__(self,field,publication):
        self.field = field
        self.publication = publication

    def researches(self):
        print(f"The field is {self.field}")
        print(f"The publication is {self.publication}")

class Professor(Teacher,Researcher):
    def __init__(self,name,subject,field,publication,experience):

        #why not using super().__init__ here?
        #when we are performing with two child classes ie., when it is inherting from 2 diff classes, if we use super().__init__ -> which init will it call (1 or 2)
        #we have a concept called MRO [Method Resolution Order] --> whenever we have multiple inheritance; it performs from left to right;
        #so if we use this, firstly it takes init of itself and then 1st class alone while leaving 2nd class

        Teacher.__init__(self, name,subject)
        Researcher.__init__(self,field,publication)
        self.experience = experience

    def show(self):
        self.teaches()
        self.researches()
        print(f"The experience is {self.experience}")

output = Professor("Aathi","Business","IT","Journal",10)
output.show()
        
#TASK 2
#Payment -> attribtues : amount -> method : to show amt
#Discount -> attributes : percentage method : to show discount
#Online order -> method -> cal final amount after discount

class Payment():
    def __init__(self,amount):
        self.amount = amount
    
    def show_amt(self):
        print(f"The amount is {self.amount}")

class Discount():
    def __init__(self,percentage):
        self.percentage = percentage
    
    def show_discount(self):
        print(f"The discount is {self.percentage}")

class Onlineorder(Payment, Discount):
    def __init__(self, amount, percentage):

        #calling the parent constructor
        Payment.__init__(self,amount)
        Discount.__init__(self,percentage)

    def final(self):
        discount_amount = self.amount * (self.percentage / 100)
        final_amount = self.amount - discount_amount 
       
        self.show_amt()
        self.show_discount()
        print(f"The final amount is {final_amount}")

result = Onlineorder(5000,10)
result.final()



