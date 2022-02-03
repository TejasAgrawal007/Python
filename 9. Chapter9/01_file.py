# use open function to read the file content
# f = open('sample.txt', 'r')
f = open('sample.txt') # By default the mode is r
# data = f.read()  
data = f.read(5)  # Read first 5 char form the file
print(data)
f.close();