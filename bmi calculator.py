# BMI = (weight in pounds x 703)/ height in inches X height in inches)
name = input("Enter your name: ")
weight = int(input("Enter your weight in pounds: "))
print (weight)
height = int(input("Enter your height in pounds: "))
BMI = (weight * 703) / (height * height)
print(BMI)
# Underweight = <18.5
# Normal weight = 18.5–24.9
# Overweight = 25–29.9
# Obesity = BMI of 30 or greater
if BMI >0:
    if (BMI <18.5):
        print(f'You are underweight {name}')
    elif  (BMI <= 24.9):
        print("You are normal weight" + name)
    elif (BMI <=29.9):
        print("You are  Overweight" + name)
    elif (BMI >30):
        print("You are Obese" + name)
    else:
        print('Enter Valid inputs' + name)
        