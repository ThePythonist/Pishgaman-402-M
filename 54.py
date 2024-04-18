def is_perfect(n):
    divs = []
    for i in range(1, n):
        if n % i == 0:
            divs.append(i)

    # print(divs)

    if sum(divs) == n:
        return True
    else:
        return False


print(is_perfect(28))
