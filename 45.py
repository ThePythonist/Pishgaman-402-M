numbers = []

for i in range(4):
    x = input("Enter any number : ")
    try:
        x = float(x)
        if str(x)[-2:] == ".0":
            numbers.append(int(x))
        else :
            numbers.append(x)
    except ValueError:
        pass

print("The numbers are", numbers)
