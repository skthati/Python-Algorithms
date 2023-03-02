
# BMI Calculator

weight = float(input("Enter the weight to calculate BMI: "))
height = float(input("Enter the height in meters to calculate BMI: "))

bmi = weight/(height * height)
bmi = round(bmi, 2)


print(bmi)
    

