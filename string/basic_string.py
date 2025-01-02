# string is immutable in python
# we can't change indivisual character in python

name = "Bhagya"
print(f'length of', name, 'is', len(name))

# slicing in str

print(name[1:3]) # index 1 to 2, 3 not incuding
print(name[-5 : -2]) # name[1 : 4]
print(name[ : 4]) # name[0 : 4]
print(name[1 : ]) # name[1 : len(name) - 1]
print(name)