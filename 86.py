lines = open("words.txt").read()
lines = lines.split("\n")

for i in lines:
    if i.isdigit():
        print(i)
