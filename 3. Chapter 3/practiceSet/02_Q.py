letter = '''Dear <|name|> ,
            Gretting from ABC Compony coding House.
            I am Happy To Tell You That you are Selected!
            Have a Grate day ahead,
            Bill
            Date:<|date|>
        '''

# print(letter)


name = input("Enter Your Name: ")
date = input("Enter Your Date: ")


letter = letter.replace("<|name|>", name)
letter = letter.replace("<|date|>", date)
print(letter)