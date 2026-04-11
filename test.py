
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
    
    @staticmethod
    def pattern(n):    
        n = 5
        for i in range(1,n+1):
            print("*" *i)
        
        
class C(B,A):
    
    def addition(self,num1,num2):
        num1=int(input("enter num1 "))
        num2=int(input("enter num2 "))
        print("result is :",num1 + num2)


obj=C()
obj.Number_ser()
obj.addition(15,15)
obj.multiplication(1,2)
obj.pattern(1)

