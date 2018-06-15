# Coding challenge part 4

# Create a BMI calculator, BMI which stands for Body Mass Index can be calculated using the formula:

#  BMI = (weight in Kg)/(Height in Meters)^2.

# Write python code which can accept the weight and height of a person and calculate his BMI.

# note: Make sure to use a function which accepts the height and weight values and returns the BMI value.

def bmiCalc(weight, height):
    bmi = weight/(height**2)
    return(bmi)

jeff_bmi = bmiCalc(56, 2.8)
print("Jeff's BMI is " + str(round(jeff_bmi, 3)))