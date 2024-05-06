lines = open("words.txt").read().split("\n")
has_digit = []

for line in lines:
    if not line.isdigit():
        for char in line:
            if char.isdigit():
                has_digit.append(line)
                break

# print(list(set(has_digit)))
print(has_digit)
