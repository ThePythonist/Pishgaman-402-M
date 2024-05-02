lines = open("words.txt").readlines()
five_letters = []

for i in lines:
    if len(i) == 6:
        five_letters.append(i)

# print(five_letters)

open("five_letters.txt", "w").writelines(five_letters)
