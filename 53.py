def decsending(items):
    # return sorted(items)[::-1] #1
    return sorted(items, reverse=True)  # 2


print(decsending([1, 3, 2, 8, 7, 6, 5, 4]))
