# def checknumber(x):
#     if type(x) in [int, float]:
#         # print("Okay continue")
#         return "Number"
#     else:
#         # print("Not okay")
#         return "Not Number"
#
# # checknumber(16)
#
# if checknumber(11) == "Number":
#     print("Yes")
# else:
#     print("No")

# -------------------------------------------

def checknumber(x):
    if x % 2 == 0:
        # print("Even")
        return "Even"
    else:
        # print("Odd")
        return "Odd"


# checknumber(14)
# n = int(input("Enter n : "))
# print(checknumber(n))


# if checknumber(8) == "Even":
#     print("Pasokh zoj ast")

# numbers = [11, 4, 2, 3, 5, 12, 16]
# for i in numbers:
#     print(checknumber(i))


# print(checknumber(12))

#
# def gozinesh(x):
#     if x % 2 == 0:
#         print(x)
#
#
# numbers = [11, 4, 2, 3, 5, 12, 16]
# for i in numbers:
#     gozinesh(i)
