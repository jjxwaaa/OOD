print(" *** Wind classification *** ")
speed=input("Enter wind speed (km/h) : ")
speed=float(speed)
if speed < 52.00:
    strom = 'Breeze.'
elif speed >= 52.00 and speed < 56.00:
    strom = 'Depression.'
elif speed >= 56.00 and speed < 102.00:
    strom = 'Tropical Storm.'
elif speed >= 102.00 and speed < 209:
    strom = 'Typhoon.'
else:
    strom = 'Super Typhoon.'
print("Wind classification is",strom)


 