print(" *** String count ***")
m = input("Enter message : ")
upper = []
lower = []
for i in m:
    if (i.isupper()):
        upper.append(i)
    elif (i.islower()):
        lower.append(i)
upper.sort()
lower.sort()
print("No. of Upper case characters :",len(upper))
upper = list(dict.fromkeys(upper))
print("Unique Upper case characters :",'  '.join(upper)," ")
print("No. of Lower case Characters :",len(lower))
lower = list(dict.fromkeys(lower))
print("Unique Lower case characters :",'  '.join(lower)," ")