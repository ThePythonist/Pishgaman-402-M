lines = open("words.txt").readlines()

for i in lines:
    # print(f"{i}:{len(i)}")
    if len(i) == 6:
        print(i)
