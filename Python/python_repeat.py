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


### multiple choice program  Line 14
# print("****************multiple choice program  Line 14*****************")
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

## Set for math purpose

# set_1 ={1,2,3,4}
# set_2 ={4,5,6}
# set_3 = (set_1).union(set_2)  ### unique values ...
# print(set_3)
# set_3 = (set_1).intersection(set_2)  ### common values ...
# print(set_3)

########## dictionary
# dict_animal = {"table" : ("a piece of furniture","list of fact & figures"),
#                "cat":"a small animal"}
# print(dict_animal)


############# set
# subjects_cls ={
#     "python","java","c++",
#     "java","python","c",
#     "javascript"
# }
# print(len(subjects_cls))

# marks = {}
# x= int(input("enter phy:"))
# marks.update({"phy":x})
# x= int(input("enter math:"))
# marks.update({"math":x})
# x= int(input("enter eng:"))
# marks.update({"eng":x})

# print(marks)

# set_20 = {"9","9.0"}
# print(set_20)


# count =1
# while count<=5:
#     a,b=50,20
#     c=a+b
    
#     print(count,c)
#     count +=1

# print(count)    

# cout = 10
# while cout >= 1:

#     print(cout)
#     cout -= 1

# print("End")    
########### numbers 1 to 100
# num_1 = 10

# while num_1 >=1:

#     print(num_1)
#     num_1 -=1

# while True:
#     print("Hi !")

### multipliaction of n number

# num = int(input("enter any number :"))
# i = 1
# while i <= 10 :
    
#     print(num *i )
#     i+=1
############## print numbers from list    
# lst =[1,4,9,16,49,25,36,49,64,81,36]
# print(lst.count(36))
# idx=0
# while idx < len(lst):
#     print(lst[idx])
#     idx +=1
############ find the x number from list

# x=49
# i=0
# while i < len(lst):
#     if (lst[i]==x):
#         print("found at index :",i)
#         break
#     else:
#         print("Finding....")    
#     i+=1
# print("Searching done...")    

# i = 1
# while i <= 100:
#     print(i,end=" ")
#     if (i == 20):
#         break
#     i += 1
    


# i = 1
# while i <=10:
#     if i == 3: 
#         i += 1
#         continue
    
#     print(i,end=" ")
#     i+=1
    



# i = 1
# while i <= 50:
#     if  35<= i <=40:
#         i+=1
        
#         continue
#     print(i)
#     i+=1      

# char = "brishtisingh"
# # idx = 0
# for ch in char:
#     if ch == 'i':
#         print("i found",end=" ")
#         # while idx < len(char):
#             # print(idx[char])
#             # idx +=1 
#         continue
#     print(ch,end=" ")
    
# lst =[1,4,9,16,49,25,36,49,64,81,36,25]

# x =25
# idx = 0
# for i in lst:
#     if i == x:
#         print("element found ",idx)
#         # break  ### stop for 1 time value
#     idx +=1    ### if break not mention it will search for another idx.(25-index=5 ,25-index=11 )

# tpl=(1,4,9,16,25,36,49,64,81,100)
# print(tpl)
# x = int(input("Enter the number from tuple"))
# idx = 0
# for i in tpl:
#     if i == x:
#         print("Searched number found at :",idx)
#     idx +=1
     
# i = 1
# while i<=10:
#     print(i*2,end=" ")
#     i+=1

# for i in range(1,11):
#     print(i*2,end=" ")
############# first n numbers sum


# n=int(input("Enter number :"))
# sum=0
# i=1
# while i <=n:
#     sum = sum + i
#     i += 1
# print(sum)



# n=5
# sum=0
# for i in range(1,n+1):
#     sum = sum +i
# print(sum)    

# n=int(input("enter number"))
# sum=0
# for i in range(1,n+1):
#     # print(i)
#     sum = sum+i
# print(sum)    

# n=int(input("Enter number for fact :"))
# fact =1
# i=1
# while i <= n:
#     fact = fact * i
#     i += 1
# print(fact)

# n=int(input("Enter number for fact :"))
# fact = 1
# for i in range(1,n+1):
#     fact = fact * i
    
# print(fact)

# cities = ["Agra","Lko","etw","Cnb"]

# def items(list):
#     for item  in list:
#         print(item,end=" ")
# items(cities)        


#### factorial using for loop 

# n = int(input("Enter any number :"))
# fact =1
# while fact <=n:

#     fact = fact * n
#     print(fact)
#     fact +=n 

# def fact_num():
      
#     n=int(input("Enter any number for factorial :"))
#     i=1
#     fact =1
#     while i<=n:
        
#          fact=fact*i
#          i+=1
#     print(fact)       
    
# fact_num()    

# def for_fact_lop():
#     n = int(input("Enter any number :"))
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i 
#     print("Factorial of given number (",n, ") is:", fact)
# for_fact_lop()          

########### convert value
# def convertor_currency(usd_val):
#     inr_val = usd_val * 92
#     print(usd_val , "USD = ",inr_val,"INR")
    
# convertor_currency(5)    

### check given number is 'odd or even'
# def odd_even():
#     n = int(input("Enter any number :"))
#     if n %2 == 0:
#         print("Even Number :",n)
#     else:
#         print("Odd Number :",n) 
        
# odd_even()           

# def recur(n):
      
#     if (n==1):
#         return 1
    
#     # print(n)
#     return n * recur(n-1)
    
# fact =recur(5)
# print(fact)


# def fact_2(n):
#     if (n==1 or n == 0):
#         return 1 
#     return fact_2(n-1) * n

# x=fact_2(5)
# print(x)

# def sum_nums(n):
#     if (n==0) :
#         return 0       
#     # print(n)
#     return sum_nums(n-1) + n    
          
# x=sum_nums(10)
# print(x)

def recur_3(lst):
    if not lst:
        return
    print(lst[0],end=" ")
    recur_3(lst[::1])

lst=[10,20,30,40]
recur_3(lst)
 
