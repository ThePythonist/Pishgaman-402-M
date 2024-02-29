# word = input("Enter any word : ")
# mirrors = ("rar", "mom", "pop", "bib")
#
# if len(word) != 1:
#     if word == word[::-1]:
#         mirrors = list(mirrors)
#         mirrors.append(word)
#     else:
#         print("False")
#
# mirrors = tuple(mirrors)
# print(mirrors)

# --------------------------------------------------------

word = input("Enter any word : ")
mirrors = ("rar", "mom", "pop", "bib")

if len(word) != 1:
    if word == word[::-1]:
        mirrors += (word,)
    else:
        print("False")

print(mirrors)
