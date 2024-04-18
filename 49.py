scores = {
    "riazi1": 15,
    "mabani computer": 20,
    "zaban omomi": 19,
    "tarikh tahlili": 7,
    "sakhteman dade": 16
}

for i,j in scores.items():
    if j >= 10:
        print(i,":","passed")
    else :
        print(i,":","failed")

grade = sum(scores.values()) / len(scores)
print(grade)
