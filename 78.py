file = open("words.txt")
lines = file.readlines()

longest = max(lines, key=len)
print(len(longest))
print(longest)

# ------------------------------------------

lines.sort(key=len)
longest = lines[-1]
print(longest)
print(len(longest))

file.close()
