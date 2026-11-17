import pickle


with open('Mypickle_dta','rb') as file:
    users = pickle.load(file)
    code = pickle.load(file)
    
# users.append("RK")    ########### users ko add krne ke liye

with open('Mypickle_dta','wb') as file:
    pickle.dump(users,file)
    pickle.dump(code,file)

print(users)