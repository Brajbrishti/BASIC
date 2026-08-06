# class Student:
#     def __init__(self,name,marks):
        
#         self.name = name
#         self.marks = marks 
#         print("Adding new student...")
    
# S1=Student("singh",99.99)
# print(S1.name,S1.marks) 

# class Student_2:
    
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks= marks
    
    
#     @staticmethod       ### works at class level, no need 'self' parameter.
#     def mesage():
#         print("Marks are the subject's of student. ")
        
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum +=val 
#         print("Hi",self.name,", avg marks are :",sum/len(self.marks))


# s1=Student_2("Raam",[60,60,60,60])
# s1.mesage()
# s1.get_avg()


# class Car_demo:
#     def __init__(self):
#         self.acc =False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("Car Started...")    
# Car1=Car_demo()
# Car1.start()            

####### Abstraction                
# class Fan:
#     def onn(self):
#         self.switch()
#         self.motor()
#         print("Fan On..")
#     def switch(self):
#         print("Switch pressed")
        
#     def motor(self):
#         print("Motor started")        
        
# f =Fan()
# f.onn()       

########## Encapsulation

# class Account:
    
#     def __init__(self,bal,acc_number):
#         self.balance=bal
#         self.acc_number=acc_number
    
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount," was debited")      
#         print("Total balance is :",self.get_balance())
        
#     def credit(self,amount):
#             self.balance += amount
#             print("Rs.",amount," is credited")      
#             print("Total balance is :",self.get_balance())
            
#     def get_balance(self):
#         return self.balance 
    
# acc1=Account(10000,12458)

# acc1.credit(50000)
# acc1.debit(15000)
# del acc1  ### deletd all data
# print(acc1)

### private attribute 'OOP
# class Account:
    
#     def __init__(self,acc_number,acc_pass):
#         self.acc_number = acc_number
#         self.__acc_pass = acc_pass
        
#     def reset_pass(self):
#         print(self.__acc_pass)

# acc_1=Account(12456,6598)        
# print(acc_1.acc_number)
# print(acc_1.__acc_pass)
# print(acc_1.reset_pass())        

class Person:
    __name ="anonymous"
    
    def __hello(self):
        print("hello everyone :")
        
    def welcome(self):
        self.__hello()    
        
p1=Person()
print(p1.welcome())    