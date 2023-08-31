def Fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return Fac (n-1)*n

num = int(input('Enter Number : '))
print(f"{num}! = {Fac(num)}")
