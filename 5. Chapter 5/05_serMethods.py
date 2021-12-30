# Creating an Empty Set

b = set()
print(type(b))

# Adding the value in empty set
b.add(4)
b.add(5)
b.add(5)
# b.add([4,5,6]) # Will throw the errror does not add a repective value
b.add((4,5,6)) # Will add a tuple cause is imMutable

# Accessig Elements

# b.add({4:5}) # Cannot add a List or dicionary
# print(b)


# Length of Set
# print(len(b))


# Removal of An item
# b.remove(5) #remove 5 of an set
# print(b)
 


# The POP() Method will remove/pop random element
# print(b.pop())
# print(b)