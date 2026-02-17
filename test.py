
class A:
    def Number_ser(self):
        for i in range(1,15,2):
            print(i)
    def multiplication(self,a,b):
        result=a*b
        print("result",result)        

    def addition(self,a,b):
        print("result is :",a+b)

obj=A()
obj.Number_ser()
obj.addition(15,10)
obj.multiplication(16,10)



