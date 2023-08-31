def	kero(current: int, n: int, times):
    global min
    if (n % 14 == 0):
        return (-1)
    if (current == n):
        if (times < min):
            min = times
        return (1)
    if (current > n or (current > 0 and current % 14 == 0)):
        return (0)
    return (kero(current + 7, n, times + 1) + kero(current + 5, n, times + 1) + kero(current + 1, n, times + 1))

n = int(input("Input number : "))
min = 99999999
result = kero(0, n, 0)
if (result == -1):
    print("Mission Failed")
    exit()
print(f"Minimum Distance is {min}")
print(f"Maximum Way is {result}")