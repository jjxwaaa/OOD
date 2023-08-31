def length(txt):     
    if txt[0:] is txt[-1:]:
        print(txt[0:], end = "*")
        return 1
    x = length(txt[:-1])
    print(txt[x], end = "*" if x % 2 == 0 else "~")
    return x + 1

print("\n",length(input("Enter Input : ")),sep="")