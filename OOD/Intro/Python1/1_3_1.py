print("*** Election ***")
input("Enter a number of voter(s) : ")
arr = [int(x) for x in input().split() if 1 <= int(x) <= 20]
f = [0 for i in range(21)]
mx = -1
for i in arr:
  if 1 <= i <= 20:
    f[i] += 1
    if(f[i] > mx):
      mx = f[i]

if(mx == -1):
  print("*** No Candidate Wins ***")
  exit(0)
ans = [x for x in range(len(f)) if f[x] == mx]

for i in ans:
  print(i, end=' ')