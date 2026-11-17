### word found and line number in given text

# def check_word_found():
#     with open("e:/new_text.txt","r") as f:
#         data=f.read()
#         print(data)
        
#     word = "good"
#     if word in data :
#         print("Found")
#     else:
#         print("Not Found")     

# def check_line_numbers():
#     word ="Raam"
#     data = True
#     line_no =1
#     with open("e:/new_text.txt","r") as f:
#         while data :
#             data =f.readline()
#             if word in data:
#                 print(line_no)
#                 return
#             line_no +=1
                
#     return -1    
# print(check_line_numbers())

# Remove any file.
# import os
# os.remove("e:/new_text.txt")    
# print("File successfully delete ho gayi!")

### find the count of even numbers , as mentioned in data
count_all=0
count=0
total_sum=0  ## for all numbers
sum = 0 ## only for even numbers
with open("e:/numbers.txt","r") as f:
    # f.write("1,4,3,6,34,22,88,53")
    data=f.read()
    print("Numbers are : ",data)
    
    nums =data.split(",")
    
    for val in nums:
        total_sum +=int(val)
        count_all +=1
        if (int(val)%2==0):  #########3  even numbers
            sum +=int(val)
            count +=1
           
print("Numbers are :",count)         
print("Sum of all given numbers",total_sum)   
print("Sum of count numbers :",sum)
            

