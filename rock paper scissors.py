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

#Write your code below this line 👇

# Recording Player Entry


result = [input("Whats Your Choice ?")]

human_choice = result[0]
print(human_choice)

# Recording computer choice
var_list = [paper , rock , scissors]

computer_choice = random.choice(var_list)
# print(computer_choice)

# Print human and computer choice

print(f"You choose {human_choice}")
print(f"Computer choose {computer_choice}")


# Adding Logic 

if human_choice == computer_choice :
    print("Draw!")

elif human_choice == "rock" and computer_choice == "paper":
    print("Computer won!")

elif human_choice == "paper" and computer_choice == "scissors":
    print("Computer won!")

elif human_choice == "scissors" and computer_choice == "rock":
    print("Computer won!")

else :
  print("You won!")
  




  
 





