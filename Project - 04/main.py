import random
number = input("Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
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

game_img = [rock, paper, scissors]
number = int(number)
new_number = random.randint(0, 2)
if number < 0 or number >= 3:
    print("You entered wrong choice.")
else:
    print(f"{game_img[number]}")
    print("Computer chose:\n")
    print(f"{game_img[new_number]}")
    if number == 0 and new_number == 2:
        print("You win")
    elif number == 1 and new_number == 0:
        print("You win")
    elif number == 2 and new_number == 1:
        print("You win")
    elif number == new_number:
        print("Draw")
    else:
        print("You lose")