f = open('poem.txt')
t = f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
      print("Twinkle is Not present")
f.close()