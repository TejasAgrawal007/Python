words = ['Donkey', 'befkuf', 'kaadu']

with open("Q4.txt") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "$%^&&^$")
    with open("Q4.txt", "w") as f:
         f.write(content)