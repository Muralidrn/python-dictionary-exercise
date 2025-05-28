"""Input:
['apple', 'banana', 'apple', 'orange', 'banana']
Output:
{'apple': ['apple', 'apple'], 'banana': ['banana', 'banana'], 'orange': ['orange']}"""

l=['apple', 'banana', 'apple', 'orange', 'banana']
d={}
for key in l:
    d[key]=[]
for key in l:
    d[key].append(key)
print(d)

#Using setdefault()
d={}
for key in l:
    d.setdefault(key,[]).append(key)

#Using defaultdict
from collections import defaultdict
d=defaultdict(list)
for key in l:
    d[key].append(key)
print(dict(d))