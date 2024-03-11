pythons = ["milad", "javad", "yasna", "mahsa"]
icdls = ["javad", "navid", "kazem", "mahsa"]
common = []

# -----------------------------------------------------------
# for i in pythons:
#     for j in icdls:
#         if i == j:
#             common.append(i)
#
# print(common)
# -----------------------------------------------------------
for i in pythons:
    if i in icdls:
        common.append(i)

print(common)
