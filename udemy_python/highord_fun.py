
# users = ["Raam","Shyam","Brihti","aman","roq","a"]
# print(min(users,key=len))

employees = ['Susan', 'Rick', 'Alice', 'Johnson', 'Ronald', 'Jeff']
# print(sorted(employees))
# print(sorted(employees , key=len))

def occurrence(word):
    return word.count("o")
print(sorted(employees,key=occurrence))

def my_reverse(word):
    return word[::-1]

print(sorted(employees,key = my_reverse))
