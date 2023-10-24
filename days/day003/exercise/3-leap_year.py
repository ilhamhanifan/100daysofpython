# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
done = False

if not done and year%4==0 and year%100!=0 and year%400!=0:
	done = True
	print("Leap year")

if not done and year%4==0 and year%100==0:
	done = True
	print("Not leap year")

if not done and year%4==0:
	done = True
	print("Leap year")

if not done:
	print("Not leap year")
