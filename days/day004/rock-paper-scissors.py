import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# WIN
# #02 10 21
# LOSE
# 01 12 #20
# DRAW
# 00 11 22

game_images = [rock, paper, scissors]

#Write your code below this line 👇
player_choice= int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[player_choice])


cpu_choice = random.randint(0,2)
print("Compute Choose:")
print(game_images[cpu_choice])
print("")

if player_choice >= 3 or player_choice < 0:
    print("invallid number")
elif player_choice == cpu_choice:
    print("Draw")
elif player_choice == 0 and cpu_choice == 2:
    print("You win")
elif player_choice == 2 and cpu_choice == 0:
    print("You lose")
elif player_choice > cpu_choice:
    print("You win")
else:
    print("You lose")
