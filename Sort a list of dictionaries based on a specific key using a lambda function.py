l=[{'name': 'John', 'age': 25}, 
   {'name': 'Jane', 'age': 22}]

s=sorted(l,key=lambda x:x["name"])
print(s)