# import time
# import random

# lis = ["red","blue","green"]
# color = random.choice(lis)
# bal = 10000
# print(f"Your balance is {bal}")

# try:
#     bet = eval(input("Enter your bet amount: "))
# except:
#     print("Enter a sufficient amount")
    

# guess = input("Enter your guess: ").lower
# if bet > bal:
#     print("Unsufficient balance")

# else:
#     if guess == color :
#             bet *= 2
#             print(f"You won {bet}")
#             bal += bet
#             print(f"Current balance is {bal}")
#     else:
#             print("You loss")
#             bal -= bet
#             print(f"Current balance is {bal}")
# print(color)

# if bal == 0:
#     print("Balance is nil")


import random
import time 

# Initial balance
bal = 10000

# Game loop
while bal > 0:
    lis = ["red", "green", "black"]
    # Player inputs
    a = input("Choose color (red, green, black): \n::::>  ").lower()
    
    if a not in ["red", "green", "black"]:
        print("Invalid color. Please choose from 'red', 'green', or 'black'.")
        continue  # Skip the current iteration if the input is invalid

    try:
        b = int(input("Enter your bet amount: \n::::>  "))
    except ValueError:
        print("Invalid input! Please enter a valid number for the bet.")
        continue

    # Check if the bet is less than or equal to the current balance
    if b <= bal:
        # Random color selection
        
        color = random.choice(lis)

        # Countdown before revealing result
        print("Spinning...")
        for i in range(1, 6):
            time.sleep(1)
            print(f"{i:02d}",end='\r')

        # Reveal chosen color
        print(f"The color is: {color}")

        # Win or lose condition
        if a == color:
            print("You won! 2x your bet!")
            bal += b  # Win: add bet amount to balance
        else:
            print("You lost!")
            bal -= b  # Lose: subtract bet amount from balance

        # Display current balance
        print("Your balance is: ", bal)
    else:
        print("Insufficient balance! Your current balance is: ", bal)

    # Check if balance is 0 after the round
    if bal == 0:
        print("Game over! You have no more balance.")
        break

# End of the game
print("Thanks for playing!")