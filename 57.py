# def is_binary(x):
#     divisors = [i for i in range(1, x + 1) if x % i == 0]
#     return True if len(divisors) == 2 else False
#
# print(is_binary(22))

def is_binary(x):
    divisors = [i for i in range(1, x + 1) if x % i == 0]
    print("Prime") if len(divisors) == 2 else None

is_binary(12)
