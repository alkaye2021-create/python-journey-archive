height_cm = float(input("what is your height (cm)? "))
weight = float(input("what is your weight (kg)? "))

height_m = height_cm / 100
bmi = weight / (height_m ** 2)

bmi = round(bmi , 2)

print(f"your bmi is {bmi}")

if bmi >= 30:
    print("you are obese")
elif bmi >= 25:
    print("you are overweight")
elif bmi < 18.5:
    print("make a sandwich")
else:
    print("you are a healthy weight")








