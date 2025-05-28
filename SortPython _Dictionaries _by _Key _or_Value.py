d={ 'banana': 1,'apple': 3, 'cherry': 2}
l=[]
for key,value in d.items():
    l.append((key,value))
#sort by keys alphabetically
sort_by_keys=sorted(l,key=lambda x:x[0])
d1={}
for key,value in sort_by_keys:
    d1[key]=value
print(d1)

#sort by values ascending order
sort_by_values=sorted(l,key=lambda x:x[1])
d2={}
for key,value in sort_by_values:
    d2[key]=value
print(d2)
