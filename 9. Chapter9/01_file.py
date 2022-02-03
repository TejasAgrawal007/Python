'''

    Types of File 
         1) Text Files
         2) Binary File


         Types of mode's
            A) r - open for reading
            B) w - open for write
            c) a - open for appending
            d) t - open for updating

'''

# use open function to read the file

# f = open('sample.txt', 'r')
f = open('sample.txt')
# data = f.read()
data = f.read(5) # Read first 5 char form the string.
print(data)
f.close()
