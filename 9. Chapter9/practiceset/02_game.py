def game():
    return 50


score = game()
with open("highscore.txt") as f:
    highStr = f.read()

if highStr=='':
    with open("highscore.txt", "w") as f:
        f.write(str(score))

elif int(highStr) < score:
    with open("highscore.txt", "w") as f:
        f.write(str(score))
