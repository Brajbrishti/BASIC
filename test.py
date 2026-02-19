
class A:
    def Number_ser(self):
        for i in range(1,15,2):
            print(i)
        
class B(A):
    def __int__(self):
        print("Child class")

    def multiplication(self,a,b):
        result=a*b
        print("result",result)        
class C(B,A):
    
    def addition(self,num1,num2):
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        print("result is :",num1 + num2)


obj=C()
obj.multiplication(5,2)
obj.Number_ser()
obj.addition(50,20)

