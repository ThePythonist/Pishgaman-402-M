number = int(input("Enter any number : "))
numbers = [444, 120, 256, 998]

if number % 2 == 0 or 99 < number < 1000:
    numbers.append(number)

print(numbers)
