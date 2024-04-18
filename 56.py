def check_binary(numbers):
    characters = {"0", "1"}
    binaries = []
    for number in numbers:
        for char in number:
            if char not in characters:
                break
        else: # Dar sorati ejra mishe ke for break nashe !!
            binaries.append(number)

    print(binaries)

items = ["24", "11101", "1111", "10101", "105"]
check_binary(items)
