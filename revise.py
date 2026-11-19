names = ['brij', 'Brishti', 'Rohan', 'Ankit', 'Bina','Rohit']
# result = {i for i in names if i.startswith('B')}
# print(result)

grouped = {}

for name in names:
    
    if name: 
        fst_letter = name[0].upper()
        
        if fst_letter not in grouped:
            grouped[fst_letter] = []
            
        grouped[fst_letter].append(name)
print(grouped)        

# sorted_names = sorted(names,key=str.lower)
# print(sorted_names)            