"""i
input : test_list = ["Gfg", "is", "Best"], subs_dict = {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}, K = 0 
Output : [5, 7, "Best"] 
Explanation : "Gfg" and "is" is replaced by 5, 7 as 0th index in dictionary value list. """

t= ["Gfg", "is", "Best","is"]
d= {"Gfg" : [5, 6, 7], "is" : [7, 4, 2]}
k=0 #replace kth value
for key in d.keys():
   for i in range(len(t)):
      if t[i]==key:
         t[i]=d[key][k]
print(t)

#list comprehension
l=[ele if ele not in d else t[ele][k] for ele in t]
print(l)