rock = "rock"
r = '''
  _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = "paper"
p = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = "scissors"
s = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random

user = input("Which do you play? Rock, Paper or Scissors? \n")
users_choice = user.lower()
if users_choice == "rock":
    print(r)
elif users_choice == "paper":
    print(p)
else:
    print(s)
rps = [rock, paper, scissors]
rps_comp = len(rps)
random_choice = random.randint(0, rps_comp - 1)
computer_output = rps[random_choice]
comp_output_str = str(computer_output)

print(comp_output_str)
if computer_output == rock:
    print(r)
elif computer_output == scissors:
    print(s)
else:
    print(p)
    

if users_choice == comp_output_str:
    print("Tie game")
elif users_choice == "rock" and comp_output_str == "paper":
    print("You lose")
elif users_choice == "paper" and comp_output_str == "scissors":
    print("You lose")
elif users_choice == "scissors" and comp_output_str == "rock":
    print("You lose")
else:
    print("You win!")
