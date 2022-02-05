with open("log.txt") as f:
    content = f.read()

if 'python' in content.lower():
    print("Yes Python is Present")
else:
    print("No Python is not present")