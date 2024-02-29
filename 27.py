# number = 1
#
# odds = []
#
# while number <= 20:
#     # if number % 2 != 0 :
#     if number % 2 == 1 :
#         odds.append(number)
#     number += 1
#
# print(odds)

odds = []

for i in range(1, 21):
    if i % 2 != 0:
        odds.append(i)

print(odds)
