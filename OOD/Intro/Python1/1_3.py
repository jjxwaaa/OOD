print('*** Election ***')
n = int(input('Enter a number of voter(s) : '))

votes = [int(x) for x in input().split()]
candidate = ""
max_ = 0
for v in votes:
    if v > 0 and v < 21:
        max_ = votes.count(v)
        print(max_)
    

if candidate == 0:
    print('*** No Candidate Wins ***')
elif n < len(votes):
    print('*** No Candidate Wins ***')
else:
    print(candidate)