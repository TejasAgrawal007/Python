num = int(input("Enter Your Number: "))
prime = True

for i in range(2, num):
    if(num%1 == 0):
        prime = False
        break

if prime:
    prime("This is a Prime Number")
else:
    prime("This is not a Prime Number")