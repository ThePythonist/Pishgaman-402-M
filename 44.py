numbers = []

for i in range(4):
    x = input("Enter any number : ")
    try:
        x = int(x)
        numbers.append(x)
    except ValueError:
        pass

print("The numbers are", numbers)
