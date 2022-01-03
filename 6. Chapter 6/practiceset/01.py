num1 = int(input("Enter The Number 1:\t"))
num2 = int(input("Enter The Number 2:\t"))
num3 = int(input("Enter The Number 3:\t"))
num4 = int(input("Enter The Number 4:\t"))


if(num1>num2):
    f1 = num1
else:
    f1 = num4

if(num2>num3):
    f2 = num2
else:
    f2 = num3


if(f1>f2):
    print(str(f1) + " is greatest")
else:
     print(str(f2) + " is greatest")
