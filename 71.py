# def find_longest(text):
#     text = text.split()
#     lengths = []
#
#     for i in text:
#         # lengths.append(len(i))
#         lengths += [len(i)]
#
#     maxlen = max(lengths)
#
#     for i in text:
#         if len(i) == maxlen:
#             print(i, ":", maxlen)
#
#
# find_longest("python is a good programming language")

# -----------------------------------------------------------------

def find_longest(text):
    text = text.split()
    print(max(text, key=len))


find_longest("python is a good programming language")

# -----------------------------------------------------------------

# print((lambda text: max(text.split(), key=len))("python is a good programming language"))
