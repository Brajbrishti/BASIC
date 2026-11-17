############ Classmethod Decorator

# class Employee_database:
    
#     company = "TVF"
#     emp_count = 0
#     tax = 10
#     bonus = 50000
    
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee_database.emp_count +=1
        
#     def show_employee(self):
#         print("Name :", self.name)
#         print("Salary :", self.salary)    
        
#     @classmethod
#     def change_company(cls,new_company):
#         cls.company = new_company    
#     @classmethod
#     def change_tax(cls,new_tax):
#         cls.tax = new_tax
#     @classmethod
#     def change_bonus(cls,new_bonus):
#         cls.bonus=new_bonus
#     # @classmethod
#     def show_compnay_detail(self):
#         print("Emp_name is :",self.name)
#         print("Company is :",self.company)
#         print("Salary is :",self.salary)
#         print("Tax is :",self.tax)
#         print("Bonus is :",self.bonus)
# print("-----------------------------------------------------------")        
#         # print("Total employees are :",self.emp_count)

# emp1 =Employee_database("Brajendra singh",2500000)
# print("-----------------------------------------------------------")
# emp2 =Employee_database("Deepika singh",2500000)
# print("-----------------------------------------------------------")
# Employee_database.change_company("Netflex")
# Employee_database.change_bonus(300000)
# Employee_database.change_tax(20)
# # Employee_database.show_compnay_detail()    
# emp1.show_compnay_detail()
# print("-----------------------------------------------------------")
# emp2.show_compnay_detail()

############ @property 
# class Student:

#     def __init__(self, name):
#         self.name = name
    
#     @property                        #### yahn par ye method h fir bhi esko variable ki tarah use kr rha hun
#     def get_name(self):
#         return self.name


# stu =Student("Rahul")
# print(stu.get_name)                 

###@property + @setter
##emp1.salary = -50000
# """Ye galat value hai ❌

# Ab hum control chahte hain ki salary read bhi ho aur update bhi, lekin validation ke saath."""

# class Employee:
#     def __init__(self,salary):
#         self.__salary = salary
    
#     @property
#     def salary(self):
#         return self.__salary    
    
#     @salary.setter
#     def salary(self,new_salary):
        
#         if new_salary < 0:
#             print("Salary can't credit")
#         else:
#             self.__salary = new_salary
            
# emp1=Employee(50000)
# print(emp1.salary)

# emp1.salary=60000
# print(emp1.salary)
#### 5 Program using property 
## creating own @decorator

# def decorator(func):
    
#     def wrapper():
#         print("before func")
#         func()
#         print("After func")
#     return wrapper    

# @decorator
# def hello():
#     print("Hello")

# hello()

#####
 
# class Rectangle:
    
#     def __init__(self,width,length):
#         self.width=width
#         self.length=length

#     @property
#     def area(self):
#         return self.length * self.width    
    
# area_1=Rectangle(5,5)
# print("Area of Rectangle is :",area_1.area)
# class Student:
#     def __init__(self,marks):
#         self.marks = float(marks)
              
#     @property
#     def student_percentage(self):
#         result= (self.marks/500)*100            
#         return result

# S1=Student(430)
# print(S1.student_percentage)
# S2=Student(477)
# print(S2.student_percentage)
##### Employee database

# class Employee_db:
    
#     def __init__(self,first_name,last_name,salary,bonus):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.salary = salary 
#         self.bonus = bonus
        
#     ### Basic entry
    
#     @property
#     def full_name(self):
#         return self.first_name +" " + self.last_name     
#     @property
#     def total_salary(self):
#         return self.salary + self.bonus
#     @property
#     def yearly_salary(self):
#         return self.total_salary * 12
#     @property
#     def emp_info(self):
#         return f"{self.full_name} earns ₹{self.yearly_salary} per year."
    
# Emp_1 = Employee_db("Braj","Singh",150000,60000)
# print(Emp_1.emp_info)    
#### class method ,
# class Student:
#     school_name = "Sarswati Inter college"
    
#     @classmethod
#     def change_sch_name(cls,new_name):
#         cls.school_name = new_name

# Student.change_sch_name("Vidya Mandir inter college")
# print(Student.school_name)

# class Student:

#     school = "SVM LKO"
    
#     def __init__(self,name):
#         self.name = name
   
# S1 = Student("a")

# S2 = Student("b")

# print(S1.school,"&",S2.school)
print("Python".zfill(10))     
