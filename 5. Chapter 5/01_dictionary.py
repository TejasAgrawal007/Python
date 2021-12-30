myDist = {
    "Tejas": "Is The Best programmer!",
    "Status": "Is a Clean Coder",
    "marks": [1,5,8],
    "anotherDict": {'Tejas': 'player'}
}
print(myDist)



print(myDist['Status'])

# Updating a List
myDist['marks'] = [45,34,1]
print(myDist["marks"])


# printing a another dictionary
print(myDist['anotherDict']['Tejas'])


# Get methods

print(myDist.get('Tejas'))  # It will print the Tejas Value 
print(myDist.get('Tejas1'))  # If value is not present Will Throw NONE

print(myDist['Tejas'])  # It will print the Tejas Value 
print(myDist['Tejas1'])  # If value is not present Will Throw Error
