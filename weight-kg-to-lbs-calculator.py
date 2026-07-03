

weight = float(input("what is your weight? "))
units = input("in what format? (kgs/lbs) ")

if units == "kgs":
    weight = weight * 2.205
    units = "lbs"

elif weight == "lbs":
    units = weight / 2.205
    units = "kgs"

else:
    print("invalid unit")

print(f"your weight is {round(weight, 2)} {units}")