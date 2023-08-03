print(" *** BMI ***")
weight,height=input("Enter your weight(kg) and height(m) : ").split()
weight=int(weight)
height=float(height)
bmi=weight/(height*height)
if bmi < 18.5:
    status = 'Below normal weight.'
elif bmi >= 18.5  and bmi < 25:
    status = 'Normal weight.'
elif bmi >= 25 and bmi < 30:
    status = 'Overweight.'
elif bmi >= 30 and bmi < 35:
    status = 'Case I Obesity.'
elif bmi >= 35 and bmi < 40:
    status = 'Case II Obesity.'
else:
    status = 'Case III Obesity.'
print("Your status is :",status)