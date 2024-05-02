def solution1(pn):
    phonenumber = f"+98{pn[1:]}"
    print(phonenumber)


# solution1(input("Enter your phone number : "))


def solution2(pn):
    phonenumber = pn.replace("0", "+98",1)
    print(phonenumber)


solution2(input("Enter your phone number : "))
