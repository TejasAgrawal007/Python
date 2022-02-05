with open("Q4.txt") as f:
    content = f.read()

content = content.replace("Donkey", "$%^&&^$")

with open("Q4.txt", "w") as f:
    content = f.write(content)