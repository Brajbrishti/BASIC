
class A:
    def Number_ser(self):
        for i in range(1,15,2):
            print(i)
    def addition(self,num1,num2):
        num1=int(input("enter num1"))
        num2=int(input("enter num2"))
        print("result is :",num1 + num2)

obj=A()
obj.addition(15,45)
obj.Number_ser()
