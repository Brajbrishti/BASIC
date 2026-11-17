import pickle

with open('Mypickle_dta','rb') as file:
    db_emp=pickle.load(file)
    db_code=pickle.load(file)
    print(db_emp)
    print(db_code)
    
