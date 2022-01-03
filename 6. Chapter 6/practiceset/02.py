sub1 = int(input("Enter the first subject marks:\t"))
sub2 = int(input("Enter the secound subject marks:\t"))
sub3 = int(input("Enter the Third subject marks:\t"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are failed cause you have less than 33% in one of these subject")
elif(sub1 + sub2 + sub3)/3 < 40:
    print("you are failed due to total prcentage less than 40")
else:
    print("Conguralations! You are Passeed")
