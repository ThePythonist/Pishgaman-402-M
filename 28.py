# entry = None
#
# while entry != "exit":
#     entry = input("Type something : ").lower()
# else:
#     print("Entry turned into exit")


flag = 1

while flag:
    entry = input("Type something : ").lower()
    if entry == "exit":
        flag = 0
else:
    print("Flag turned into exit")
