# import time
# import random

# bal = 20000
# print(f"Your current balance is {bal}")

# lis = ["red","green","blue"]

# while bal > 0:
#     guess = input("Enter your guess: ")
#     bet = eval(input("Enter your bet amount: "))
    
#     color = random.choice(lis)

#     if guess not in lis:
#         print("Please choose from [red,green,blue]")
#         continue

#     for i in range(5,0,-1):
#         time.sleep(1)
#         print(f"{i:02d}",end='\r')

#     if bet <= bal:
#         if guess == color:
#             print(f"You won, your balance is now {bet}")
#             bal += bet
#         else:
#             print("You lost ",bet)
#             bal -= bet
#         print(bal)
#     else:
#         print("Unsufficient balance")

#     if bal == 0:
#         print("You have no more balance")

# print("Thanks for playing")

# import random
# for i in range(1,31):
#     num = random.randint(1,40)`
#     print(num)

# def sort(a):
#     for i in range(1,len(a)):
#         cur = a[i]
#         prev = i-1
#         while prev >= 0 and a[prev] > cur:
#             a[prev+1] = a[prev]
#             prev -= 1
#         a[prev+1] = cur
#     for i in range(len(a)):
#         print(f"{a[i]}",end=" ")

# lis = [23,4,15,56,44,32]
# sort(lis)

def a(x,y=2):
    print(f"X={x} \n Y={y}")

a(2)