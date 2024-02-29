# number = 1
#
# evens = []
#
# while number <= 20:
#     if number % 2 == 0 :
#         evens.append(number)
#     number += 1
#
# print(evens)


evens = []

for i in range(1, 21):
    if i % 2 == 0:
        evens.append(i)

print(evens)