
class A:
    def Number_ser(self):
        for i in range(1,15,2):
            print(i)
    def multiplication(self,a,b):
        result=a*b
        print("result",result)        

<<<<<<< Updated upstream
    def addition(self,a,b):
        print("result is :",a+b)

obj= A()
obj.Number_ser()
obj.addition(15,100000)
obj.multiplication(16,10)
=======
    def addition(self,num1,num2):
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        print("result is :",num1 + num2)
class B(A):
    def __int__(self):
        print("Child class")
obj=B()
obj.addition(1,2)
obj.multiplication(15,15)

>>>>>>> Stashed changes

# user_input=input("Enter the string to be reversed:")
# reversed_list=""
# for ch in user_input:
#     reversed_list=ch+reversed_list
# print(reversed_list)

