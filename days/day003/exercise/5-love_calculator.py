print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combinedname = name1.upper() + name2.upper()
res1 = combinedname.count("T")
res1 += combinedname.count("R")
res1 += combinedname.count("U")
res1 += combinedname.count("E")

res2 = combinedname.count("L")
res2 += combinedname.count("O")
res2 += combinedname.count("V")
res2 += combinedname.count("E")

score = int(str(res1) + str(res2))

if score < 10 or score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
