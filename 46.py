numbers = []
x = None

while x != "exit":
    x = input("Entry : ")
    try:
        x = float(x)
        if str(x)[-2:] == ".0":
            numbers.append(int(x))
        else:
            numbers.append(x)
    except ValueError:
        pass

print("Numbers : ", numbers)

# for i in numbers:
#     print(i, type(i))
