myDict = {
    "pankha": "Fan",
    "kach": "Glass",
    "vastu": "Item"
}

print("Option are ", myDict.keys())
a = input("Enter The Hindi Word\n")

print("The Meaning of your word is: ", myDict.get(a))