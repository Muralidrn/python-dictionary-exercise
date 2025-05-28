d={'a': 1, 'b': 2,'c':3,'d':5,'f':7}
key=input("enter a key ")

"""if d.get(key)==None:
    print("key not found")
else:
    print(d.get(key))"""

print(d.get(key,"key not found"))