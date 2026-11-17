# class LoginSystem:
    
#     def login(self,username,password):
        
        
#         if self.__validate_user(username,password):
#             return "Login Successful"
#         else:
#             return "Invalid Login" 
        
#     def __validate_user(self,username,password):
        
#         if username == "Singh" and password == "3565":
#             return True
                       
#         return False
# user = LoginSystem()
# print(user.login("Singh","3565"))            


# class Test_1:
#     def __init__(self,name,marks):
        
#         self.name = name 
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print("Hello ") 

# tst=Test_1("lado",99)
# print(tst.name)           
# tst.hello()
        

# from abc import ABC, abstractmethod

# class Employee(ABC):

#     @abstractmethod
#     def calculate_salary(self):   #### es function ko compulsary h child class mei krna 'abstraction' rule h
#         pass        
# class FullTimeEmployee(Employee):

#     def calculate_salary(self):
#         print("Salary: ₹50,000")
# class PartTimeEmployee(Employee):

#     def calculate_salary(self):
#         print("Salary: ₹20,000")    
        
# class Intern(Employee):
    
#     def calculate_salary(self):
#         print("Not defined for Intern employee :")

# emp3 = Intern()              
# emp1 = FullTimeEmployee()
# emp2 = PartTimeEmployee()

# emp1.calculate_salary()
# emp2.calculate_salary()        
# emp3.calculate_salary()

# from abc import ABC, abstractmethod 

# class Payment(ABC): 
#     @abstractmethod 
#     def pay(self, amount): 
#         pass

# class UPI(Payment):
#     def pay(self, amount):
#         print(f"₹{amount} paid using UPI")

# class CreditCard(Payment): 
#     def pay(self, amount): 
#         print(f"₹{amount} paid using Credit Card")
        
# upi = UPI() 
# upi.pay(500) 
# card = CreditCard()
# card.pay(1000)

##### hierarchcal inharitance parent calculator>addition>substraction>multiplication
# from abc import ABC, abstractmethod


# class Calculator(ABC):

#     @abstractmethod
#     def calculate(self, a, b):
#         pass


# class Addition(Calculator):

#     def calculate(self, a, b):
#         return a + b


# class Subtraction(Calculator):

#     def calculate(self, a, b):
#         return a - b


# class Multiplication(Calculator):
#     def calculate(self, a, b):
#         return a * b
    
# add = Addition()
# sub = Subtraction()
# mul = Multiplication() 

# print(add.calculate(15,5))   
# print(sub.calculate(15,5))
# print(mul.calculate(15,5))

#### multilevel inheritance 

# class Calculator:

#     def __init__(self):
#         print("This is Calculator")

# class Addition(Calculator):
    
#     def add(self, a, b):
#         return a + b

# class AdvancedAddition(Addition):
    
#     def add_three_numbers(self, a, b, c):
#         return self.add(a, b) + c
    
# obj=AdvancedAddition()
# print(obj.add(10,20))
# print(obj.add_three_numbers(12,30,25)    )

# class Addition:
#     def add(self,a,b):
#         return a+b
    
# class Subtraction:
#     def sub(self,a,b):
#         return a-b
# class Calculator(Addition,Subtraction):  #### multiple inheritance 
#     def show(self):
#         print("The Addition and Subtraction are :")

# obj=Calculator()
# print(obj.add(10,50))
# print(obj.sub(50,10))
    
        