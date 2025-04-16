import random
possible_choices = ["r", "p", "s"]


def get_user_input():
    while True:
        user_input = input("Choose rock, paper, or scissors (r/p/s): ").lower()
        if user_input in possible_choices:
             return user_input
        else:
            print("Invalid choice.") # notice how this will just rerun the while loop

def get_computer_choice():
    possible_choices = ["r", "p", "s"]
    computer_choice = random.choice(possible_choices)
    return computer_choice

def display_choices(user_input, computer_choice):
    print("You chose:", user_input )
    print("The computer chose:", computer_choice)
    
def determine_winner(user_input, computer_choice):
    if user_input == computer_choice:
            print("The result was a draw.")
    elif ((user_input == "p" and computer_choice == "r") or (user_input == "r" and computer_choice == "s") or (user_input == "s" and computer_choice == "p") ):
            print("You won.")
    else:
        print("The computer won.")

     
    

def play_game():
     while True:
          user_input = get_user_input()
        
          computer_choice = random.choice(possible_choices)

          display_choices(user_input, computer_choice)

          determine_winner(user_input, computer_choice)

          replay_answer = input("Do you want to play again (y/n)?").lower()
          if replay_answer == "n":
               break
          else:
               continue

play_game()