lines = open("words.txt","r").readlines()

for i in lines:
   if "ing" in i:
       print(i)

