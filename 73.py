users = [
    "09396908964",
    "09129232905",
    "09220878392",
]


# def send_message(user):
#     message = f"""
# Moshtarake gerami {user}
# shoma 85% az basteye khod ra
# masraf kardeid.
# """
#     print(message)

def send_message(user):
    message = """
Moshtarake gerami {}
shoma 85% az basteye khod ra
masraf kardeid.
""".format(user)
    print(message)


for x in users:
    send_message(x)
