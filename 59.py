def evenorodd(number):
    print("The number is even") if number % 2 == 0 else print("The number is odd")


def isnumber(entry):
    if entry.isdigit() == True:
        entry = int(entry)
        evenorodd(entry)
    else:
        print("Entry is not a number")


isnumber("45")
