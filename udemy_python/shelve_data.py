import shelve

code =[1,2,3,4,5,6]

s = shelve.open('Myshelve_data')
s['code']= code
print(list(s.keys()))

del s ['code']
print(list(s.keys()))

s.close()












