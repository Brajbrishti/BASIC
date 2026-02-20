class Triangles:
    def triangle(self):
        row = 6
        for i in range(row):
            for j in range(row - i - 1):
                print(" ",end="")
            for j in range( 2 * i + 1 ):
                print("*",end="")
            
            print()
         
    def rightangle(self):
        row = 8
        for i in range(row):
            for j in range(row - i - 1):
                pass
            for j in range( 2 * i + 1 ):
                print("*",end="")
            print()
obj = Triangles()
obj.triangle() 
obj.rightangle()   
    

        