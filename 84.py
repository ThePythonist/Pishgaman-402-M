with open("words.txt") as f:
    f = f.readlines()
    open("reversedwords.txt", "w").writelines(f[::-1])
