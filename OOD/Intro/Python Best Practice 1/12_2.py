print(" *** Rank score ***")
Input = list(map(str,input("Enter ID and Score end with ID : ").split()))
ID = Input[-1]
Input.pop()
new = {}
for id in range(0,len(Input),2):
    new[Input[id]] = float(Input[id+1])
print(Input)
print(ID)
print(new)
new2 = dict(sorted(new.items())) #เรียง key
new2 = dict(reversed(list(new2.items())))
new2 = dict(sorted(new2.items(), key=lambda item: item[1])) #เรียง value
# print(new2)
ans = list(set(new2.values()))
for id in new:
    if (ID == id ):
        ans = len(ans) - ans.index(new[id])
        break
if (type(ans) == list):
    ans = "Not Found"
print(ans)