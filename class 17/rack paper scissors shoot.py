# Step 1: Import the random module.

# Step 2: Start a while True loop so the game can repeat for multiple rounds.

# Step 3: Ask the player for their choice - rock, paper, or scissors.

# Step 4: Generate a random number from 1 to 3 using random.randint(1, 3).

# Step 5: Use if/elif to turn that number into the computer's move: 1 becomes rock, 2 becomes paper, and anything else becomes scissors.

# Step 6: Print both the player's and computer's choices using an f-string.

# Step 7: Compare the two choices with if/elif to decide whether it's a tie, a win, or a loss, printing the result.

# Step 8: Ask if the player wants to play again, and break out of the loop if the answer isn't "y".



import random
while True:
    user = str(input("choose one rock paper or scissors"))
    computer = random.randint(1, 3)
    if computer == 1:
        computer_action = "rock"
    elif computer == 2:
         computer_action = "paper"
    else:
         computer_action = "sicssors"
    if user == computer_action:
         print("tie")
    elif user == "rock" and computer_action == "paper":
         print(" the computer won a point!!!")
    elif user == "rock" and computer_action == "sicssors":
         print("the user won a point!!!")
    elif user == "paper" and computer_action == "rock":
         print("the user won a point")
    elif user == "scissors" and computer_action == "paper":
         print("user won a point")
    elif user == "paper" and computer_action == "scissors":
         print("the computer got a point")
    elif user == "scissors" and computer_action == "rock":
         print("computer got a point")
    again = str(input("do you want to play again?"))
    if again != "yes":
         break