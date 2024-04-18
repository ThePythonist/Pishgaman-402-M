def adder(number):
    figures = [int(i) for i in str(number)]
    return sum(figures)


print(adder(983))
