# Step 1: Import the random module.

# Step 2: Set a variable playing to True to control the game loop.

# Step 3: Generate a secret number between 0 and 9 using random.randint(0, 9), converting it to a string.

# Step 4: Print instructions explaining the guessing game to the player.

# Step 5: Start a while playing loop that keeps asking for a guess.

# Step 6: If the guess matches the secret number, print a winning message showing the number, then break out of the loop.

# Step 7: Otherwise, print a message asking the player to try again, and the loop continues.


import random
qwerty = True
devitha = random.randint(0, 9)
print("these are the instructions for the secret number guesser")
print("there are numbers from 0 to 9 ")
print("you should guess the number that the computer will randomly pick ")
while qwerty:
    user = int(input("enter you guess"))
    if devitha == user:
        print("you won 🥇 thank you for playing secret number guesser")
        break
    else: 
        print("try again")
