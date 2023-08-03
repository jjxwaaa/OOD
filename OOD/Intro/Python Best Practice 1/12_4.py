print("*** String Rotation ***")
a, b = input("Enter 2 strings : ").split()
i = 1
x = a[-1] + a[:len(a)-1]
y = b[1:len(b)] + b[0]
print(i,x,y)
while (a!=x or b!=y):
    i+=1
    x = x[-1] + x[:len(x)-1]
    y = y[1:len(y)] + y[0]
    if (i <= 5):
        print(i,x,y)
    elif (a==x and b==y and i==6):
        print(i,x,y)
if (i > 6):
    print(" . . . . . ")
    print(i,x,y)
print(f"Total of  {i} rounds.")