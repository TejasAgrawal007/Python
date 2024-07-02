myDist = {
    "Tejas": "Is The Best programmer!",
    "Status": "Is a Clean Coder",
    "marks": [1, 5, 8],
    "anotherDict": {'Tejas': 'player'},
    1: 2
}
print(myDist)


# Dictionary Methods

# 1. Print the key of dictionary
# print(list(myDist.keys()))


# 2. printing the value of the dictionary
# print(myDist.values())

# 3. printing the (key values) of all content of the dictionary
# print(myDist.items())


# 4. Updating the dictionary
# tejas = {
#     "Teach": "Mindspace Teach Name is Tejas",
#     "XYZ": "ABC is the Best Person"
# }

# myDist.update(tejas)
# print(myDist)


# ***---Interview Questions---***

# printing the value associated with key value
print(myDist.get("Tejas"))
# if Keys are not present return none


# printing the value associated with key value
print(myDist['Tejas'])
# if Keys are not return error like --> print(myDict['Tejas1'])
