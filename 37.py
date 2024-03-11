tedad = int(input("How many entries : "))
numbers = []

for i in range(tedad):
    x = float(input("Enter any number : "))
    numbers.append(x)

print(max(numbers))
