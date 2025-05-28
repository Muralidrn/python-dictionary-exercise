""" For example, in d = {"A": [1, 2, 2], "B": [3, 4, 5, 3], "C": [6, 7, 7, 8]}, key "C" has the most unique values ({6, 7, 8} → 3"""

d = {"A": [1, 2, 2], "B": [3, 4, 5, 3], "C": [6, 7, 7, 8]}
most=max(d,key=lambda x:len(set(d[x])))
print(most)

"""d = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88} then the output will be Jaguar"""

most1=max(d,key=lambda x:d[x]) # x-take key and return key
print(most1)
most1=max(d.items(),key=lambda x:x[1])# x-take both key and value
print(most1)