import random
from art import rock, paper, scissors

print("Welcome to our game ... have fun")
ask_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print("You chose:")

if ask_user == 0:
  print(rock)

elif ask_user == 1:
  print(paper)

elif ask_user == 2:
  print(scissors)

else:
  print("Invalid number")

choices = [rock, paper, scissors]

computer_choice = random.randint(0, 2)
computer = choices[computer_choice]
print("Vs")

print("Computer chose:")


print(computer)


if ask_user == 0 and computer_choice == 0:
  print("It's a draw")

elif ask_user == 0 and computer_choice == 1:
  print("You lose")

elif ask_user == 0 and computer_choice == 2:
  print("You win")


if ask_user == 1 and computer_choice == 0:
  print("You win")

elif ask_user == 1 and computer_choice == 1:
  print("It's a draw")

elif ask_user == 1 and computer_choice == 2:
  print("You lose")

if ask_user == 2 and computer_choice == 0:
  print("You lose")

elif ask_user == 2 and computer_choice == 1:
  print("You win")

elif ask_user == 2 and computer_choice == 2:
  print("It's a draw")

elif ask_user > 2:
  print("Please enter a correct number")
