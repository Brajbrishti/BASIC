# code for multiplication
# code for division
# test input value in a variable and check output without using print()

# name = input("name :")
# age = 15
# age = int(input("enter ur age :"))
# if age > 18:
#     print("Adult")
# else:
#     print("Minor")



# choice =input ("Enter choice (+,-,*) :")

# a=int(input("enter no."))
# b=int(input("enter no."))


# if choice == "+":
#     c=a+b
#     print(c)
    
# elif choice == "-":
#     c=a-b
#     print(c)
  
# else:
#     print("try again ")
    
    
# food = input("food :")
# eat = "yes" if food=="cake" else "no"
# print(eat)            

# food = input("food :")
# print("sweet") if food=="cake" or food == "kala jamun"else print("no sweet")
# 
# age = int(input("Enter your age and check Vote status"))
# vote = ("yes" , "no") [age <18]
# print(vote)

# print(input("enter name name is : "))
# str ="OM Shivay" 
# char=str[1:len(str)]
# print(char)

# str= "apple"
# str=str.capitalize()
# print(str)
# print(str)
# print(str.replace("p","P"))


# num = int(input("enter a number ,to be multiple of 7 : "))
# if num % 7 ==0:
#     print("num is multiple of 7 : ",num)
# else:
#     print("Num is not multiple of 7 : ",num)    

# name= "Raam"
# print(name[:5])
# line1 = "welcome to python code.com" 
# print(line1.find("come"))
# print(line1.count("o"))



# line2 = [30,10,25,90,12,10,20,10]
# line2.sort(reverse=True)
# print(line2)
# line2.sort()
# print(line2)
# line2.append(100)
# print(line2)
# line2.insert(5,101)
# print(line2)
# line2.remove(10)
# print(line2)

# print(line2)
# line2.pop(2)
# print(line2)
# print(line2.count(10))
# line2.sort()
# print(line2)
# set_1=set(line2)
# print(list(set_1))

# movie_list = []
# name_movies = input("enter any 3 movies name")
# if len(name_movies.split())==3:
#     for name in name_movies.split():
#         movie_list.append(name)
#     print(movie_list)
# else:
#     print("entered movies are more then no.")    
    
# movie_list = []
# for i in range (3):
#     movie=input(f"Enter movie {i+1} name: ")
#     movie_list.append(movie)
# print(movie_list)    


# movies_list=[]
# count =1
# while count<=3:
#     movie=input(f"Enter movie {count} name:")
#     movies_list.append(movie)
#     count +=1
# print(movies_list)    

# movies = [] 
# movies.append(input("enter name 1:"))
# movies.append(input("enter name 2:")) 
# movies.append(input("enter name 3:")) 
# print(movies) 
# lstt_1= [1,"cda","abc",1]
# lstt_2=lstt_1.copy()
# lstt_2.reverse()
# if (lstt_2 == lstt_1):
#     print("Palindrorme")
# else:
#     print("not a palindrome")

# word = input("enter a word to check palindrome :")
# if word == word [::-1]:
#     print("Palindr")
# else:
#     print("not palindr")    

# student= {
#     "name " :"Brishti",
#     "subjetc":{    
#         "hindi":99,
#         "eng":100,
#         "math":98
#     }
# }
# print(student["subjetc"])

# word = input("Engter the word :")
# reverse = ""
# for ch in word:
#     reverse = ch + reverse
# if word == reverse:
#     print("Palindrome")
# else:
#     print("No Palindrome")        


# dict_student_cont = {
#     "name":"Raam",
#     "subjects":{
#         "hindi":98,
#         "eng":99,
#         "math":100
#     }
# }
# new_dict= {"city":"LKO"}
# dict_student_cont.update(new_dict)

# try :
#       print(dict_student_cont)    
# except:
#     print(dict_student_cont.get("name"))
        
# finally:
#     print("Program done !")        
    



# lst = [[12,34,24],[20,4,5],[89,65]]
# flt = [a for x in lst for a in x]
# print(flt)
# flt = []
# for x in lst:
#     for a in x:
#         flt.append(a)
# print(flt)

# age_vote = int(input("Check age  for vote"))
# vote = ("no" , "yes") [age_vote > 18]
# print(vote)
