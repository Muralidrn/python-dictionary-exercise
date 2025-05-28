s = "hello world, have a great day"
d= {'hello': 'hi', 'world': 'earth'}

s=s.replace(',',' ')
s=' '.join([d.get(word,word) for word in s.split()])
print(s)