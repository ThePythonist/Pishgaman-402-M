def check_duplicate(word):
    if len(word) == len(set(word)):
        return False
    else :
        return True

print(check_duplicate("ted"))
