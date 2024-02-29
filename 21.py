age = int(input("Enter your age : "))

allowed = ["kian", "mina", "pedram", "aria"]

if age >= 18:
    name = input("Enter your name : ")
    allowed.append(name)

print("Allowed users :", allowed)
