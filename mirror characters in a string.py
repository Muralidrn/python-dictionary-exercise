"""
Input : N = 3
        paradox
Output : paizwlc
We mirror characters from position 3 to end.

Input : N = 6
        pneumonia
Output : pneumlmrz"""

original = 'abcdefghijklmnopqrstuvwxyz'
reverse = 'zyxwvutsrqponmlkjihgfedcba'
d = dict(zip(original,reverse))
print(d)
n=3
s="paradox"
l=list(s)
for key in range(n-1,len(l)):
    l[key]=d[l[key]]
s=''.join(l)
print(s)
