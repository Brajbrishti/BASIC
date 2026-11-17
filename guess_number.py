#### Code about guess a number between ' 1 to 100'
### Small game have fun !!

# import random

# target = random.randint(1,100)
# while True:
#     userChoice =input ("Guess the number or want to Quit ' Q' :")
#     if (userChoice == "Q"):
#         break
    
#     userChoice = int(userChoice)
#     if userChoice == target:
#         print("Success : Good guess")
#         break  
    
#     elif(userChoice < target ):
        
#         print("Guess number is SMALL,take BIG one !")
#     else:
#         print("Guess number is BIG, take SMALL one !")
        
        
    
# print("--------------Game Over----------- !!!")        


#### Random password generator at length of 8,9,10....!
import random
import string

pass_len = 4
password =""

charValue = string.ascii_letters 

for i in range(pass_len):
    password += random.choice(charValue)

print("Password is :",password)
    
############### user login

username = input("Enter username: ")
user_password = input("Enter password: ")

if user_password == password:
    print("Login Successful")
else:
    print("Invalid Password")

    
        
    



