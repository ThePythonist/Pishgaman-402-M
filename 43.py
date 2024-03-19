primes = []

for i in range(1, 101):
    for j in range(2, i):
        if i % j == 0:
            break # halgheye dovom (j) ra break mikonad
    else:
        primes.append(i)

print(primes)
