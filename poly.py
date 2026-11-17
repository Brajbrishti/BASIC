class Complex:
    
    def __init__(self,real,img):
        self.real =real
        self.img=img
    
    def shownumber(self):
        print(self.real,"i +",self.img,"j") 
    
    def add(self,num2):
    # def __add__(self,num2):    ### dunder function
        new_real=self.real + num2.real
        new_img=self.img + num2.img
        return Complex(new_real,new_img)
    
num1=Complex(1,3)
num1.shownumber()    
num2=Complex(3,6)
num2.shownumber()           
num3=num1.add(num2)    ### without __add__     (simple 'def add' function)
# num3=num1 + num2     ### __add__ used here
num3.shownumber()    