# create a new list

myListOne = [1,2,3,4,5,6,7,8,9,10]
myListTwo = myListOne

# print both

print(myListOne)
print(myListTwo)

# change myListOne

myListOne = [1,4,3]
# prient both again

print(myListOne)
print(myListTwo)

# note : in this we create a new reference for myListOne so no changes in myListTwo

# Example no two 

l1 = [1,2,3,4,5]
l2 = l1

#print both

print(l1)
print(l2)

# now change one value in l1

l1[0] = 10

# print both again

print(l1)
print(l2)

# note: in the second example, both l1 and l2 are pointing to the same list. So when we change a value in l1, it also changes the value in l2. This is called a reference in Python.