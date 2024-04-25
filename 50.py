# word = input("Enter any word : ")
# chars = {}
# index = 0
#
# for i in word:
#     chars.setdefault(index, i)
#     index += 1
#
# print(chars)

# ______________________________________________


# word = input("Enter any word : ")
# chars = {}
#
# for i in range(len(word)):
#     chars.setdefault(i, word[i])
#
# print(chars)

# ______________________________________________

word = input("Enter any word : ")
chars = dict(zip(word, range(len(word))))
print(chars)
