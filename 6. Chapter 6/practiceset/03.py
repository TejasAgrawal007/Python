text = input("Enter the Text:\t")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("Subscribe this" in text):
    spam = True
elif("click this" in text):
    spam =  True
else:
   spam =  False

if(spam):
    print("This Text is spam ")
else:
    print("This text is not a spam Text")