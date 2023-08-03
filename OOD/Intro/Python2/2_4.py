def hbd(age):
    i = 3
    while True:
        if age//i == 2 and age%i==0 :
            return "saimai is just 20, in base "+str(i)+"!"
        elif age//i == 2 and age%i==1 :
            return "saimai is just 21, in base "+str(i)+"!"
        i+=1

year = input("Enter year : ")

print(hbd(int(year)))