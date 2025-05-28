l=[('a', 1), ('b', 2), ('a', 3)]
d={}
for key,value in l:
    if key in d:
        d[key].append(value)
    else:
        d[key]=[value] #create list []
print(d)