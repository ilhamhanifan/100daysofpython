# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height**2
print(f"Your BMI is {bmi}, ", end="")

if bmi < 18.5:
  print("you are underweight.")
if bmi > 18.5 and bmi < 25:
  print("you have a normal weight.")
if bmi >=25 and bmi < 30:
  print("you are slightly overweight.")
if bmi >=30 and bmi < 35:
  print("you are obese.")
if bmi >=35:
  print("you are clinically obese.")
