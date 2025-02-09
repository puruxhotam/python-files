'''BANK'''

# balance = 1000
# print("Enter 1 for view balance.\nEnter 2 for deposit money.\nEnter 3 for withdraw money.")
# n = int(input("Enter one choice:"))
# if n == 1 :
#      print("Your current balance:",balance)
# elif n == 2:
#      deposit = int(input("Enter money to deposit:"))
#      print("Money is depositted successfully")
#      balance = balance + deposit
#      print("Your current balance:",balance)
# elif n == 3:
#      withdraw = int(input("Enter money to withdraw:"))
#      if withdraw <= balance :
#           print("Money withdrawn successfully")
#           print("Your current balance:",balance-withdraw)
#           balance =- withdraw
#      else:
#         print("Insufficient balance")
# else:
#     print("ERROR!!! enter a valid choice")

'''NUMBER GUESSING GAME'''

# import random
# print("Welcome in guess the number game,")
# random_number =  random.randint(1,50)
# print("Enter your guess between 1 to 50:")
# limit = 7
# for i in range(1,limit+1):
#     guess = int(input())
#     if guess > random_number:
#         print("Your guess is high, try low number.")
#         limit -= 1
#         print(f"You have {limit} chances")
#     elif guess < random_number:
#         print("Your guess is low, try high number.")
#         limit -= 1
#         print(f"You have {limit} chances")
#     elif guess > 50:
#         print("Please enter your guess between 1 to 50")
#         limit -= 1
#         print(f"You have {limit} chances")
#     else:
#         break
    
# if guess == random_number:
#     print("WOW!! you guessed it right🥳")
# else:
#     print("OOPS!! you lost all your turns.Try again")
#     print("The number was ",random_number)

'''DICTIONARY'''

# capital = {
#     "india" : "new_delhi",
#     "japan" : "tokyo",
#     "china" : "beijing",
#     "USA"   : "washington_dc",
#     "pakistan" : "karachi"
# }
# new = capital.get("india")
# print(new)
# print(capital["china"])

'''RANDOM COLOR GENERATOR'''

# import random
# print("The color bet result is ")
# choice = random.randint(1, 20)
# if choice == 1:
#     print("🔴")
# elif choice == 2:
#     print("🟡")
# elif choice == 3:
#    print("🟢")
# elif choice == 4:
#    print("🔵")
# elif choice == 5:
#    print("🟠")
# elif choice == 6:
#    print("🟣")
# elif choice == 7:
#    print("🟤")
# else:
#    print("Nothing") 

'''ROCK PAPER SCISSORS'''
 
# import random
# import time

# print("Ready, rock-paper-scissors")
# def countdown(t):
#     while t:
#         mins, secs = divmod(t,60)
#         print(f"{mins:02d}:{secs:02d}",end="\r")
#         time.sleep(1)
#         t -= 1

# countdown(3)
# print("It's a ")
# game = random.randint(1,3)
# if game == 1:
#     print("✊")
# elif game == 2:
#     print("🖐️")
# elif game == 3:
#     print("✌️")

'''TIMER''' 

# import time

# my_time = int(input("set timer:"))
# for i in reversed(range(1,my_time+1)):
#     time.sleep(1)
#     print(f"{i:02d}",end='\r')
# print("Time's up!!") 

'''CALCULATOR'''

# instruction = '''-> Type '1' for addition(+)
# -> Type '2' for subtraction(-)
# -> Type '3' for multiplication(*)
# -> Type '4' for division(/)'''
# print(instruction)
# operator = int(input("Type a choice for calculation:"))
# num1 = float(input("Enter the first number:"))
# num2= float(input("Enter the second number:"))  

# if operator == 1:
#     result = num1 + num2
#     print(result)
# elif operator == 2 :
#     result = num1 - num2
#     print(result)
# elif operator == 3 :
#     result = num1 * num2
#     print(result)
# elif operator == 4 :
#     result = num1 / num2
#     print(result)
# else:
#     print(f"{operator} isn't a valid choice, enter a valid choice")

'''FUNCTIONS'''

# def add(a, b):
#     return a+b

# print(add(5,2))

# square = lambda x: x**2 #Lambda function
# print(square(6))

# print((lambda s,t: s+t/2)(5,9)) #Lambda function in print function

# def expL(num):
#     return lambda mul_num: mul_num*num
# my_multiplier = expL(3)
# print(my_multiplier(5))

'''SORTING A LIST'''

# def arr(nums):
#     size = len(nums)
#     for i in range(0, size):
#         for j in range(i):
#             if nums[j] > nums[j+1]:
#                 temp = nums[j]
#                 nums[j] = nums[j+1]
#                 nums[j+1] = temp 

# l = [5,2,6,3,9,7]
# print("Original array")
# print(l)
# arr(l)
# print("Sorted array")
# print(l) 

'''UNIT CONVERTER'''

# print("Welcome to unit converter")
# a = '''
# 1. Feet ->
# 2. Inch ->
# 3. Centemeters ->'''
# print(a)
# n = int(input("Enter your choice:"))
# if n == 1:
#     feet_choice = '''
#     1. Feet -> Inch
#     2. Feet -> Centemeters
#     3. Feet -> Meters
#     4. Feet -> Miles'''
#     print(feet_choice)
#     n_feet = int(input("Enter an unit to convert from feet:"))
#     if n_feet == 1:
#         print("Feet -> inch")
#         feet = eval(input("Enter a feet:"))
#         inch = feet * 12
#         print(feet,"feet =", inch,"inches")
# elif n == 2:
#     print("Inch -> Feet")
#     inch = eval(input("Enter a value:"))
#     feet = inch/12
#     print(inch ,"inches =",feet,"feet")
# elif n == 3:
#     print("Centemeters")
#     n_cm = int(input("Enter an unit to be converted:"))
#     if n_cm == 1:    
#         cm = eval(input("Enter a value"))
#         print("Cm -> Inch")
#         inch = cm * 0.393 7
#         print(cm, "cm =",inch,"inches")
#     elif n_cm == 2:
#         cm = eval(input("Enter a value"))
#         print("Cm -> Feet")   
#         feet = cm / 30.48
#         print(cm,"cm =", feet,"feet")
# mtr = eval(input("Enter a value"))
# mile = eval(input("Enter a value"))
# km = eval(input("Enter a value"))

'''SWAPPING VALUES'''

# def swap(a,b):
#     print(f"Before swapping a={a} and b={b}")
#     t = a 
#     a = b 
#     b = t
#     print(f"After swapping a={a} and b={b}")
# print(swap(2,4)) #Swapping using third variable

# x = 4
# y = 8
# print(f"Before swapping X = {x} and Y = {y}")

# x = x - y
# y = x + y
# x = y - x
# print(f"After swapping X = {x} and Y = {y}")

'''SEARCHING ITEM FROM LIST'''

# def search(List):
#     item = int(input("Enter item for search:"))
#     if item in List:
#         print(f"{item} found in the list")
#     else:
#         print("Item not found")
            
# lst = [2,34,54,36,76]
# search(lst)     

'''CHECKING THE FIRST AND LAST VALUE EITHER SAME OR NOT'''

# def same_val(List):
#     first_val = List[0]
#     last_val = List[-1]
#     if first_val == last_val:
#         return True
#     else:
#         return False
# print(same_val([1,4,5,20,2,1]))
# print(same_val([28,4,5,2,5,5]))

'''CHECKING IF TWO LISTS CONTAINING SAME ELEMENTS'''

# def check_lis(lis1,lis2):
#     if len(lis1) != len(lis2):
#          return "Different length"
#     else:
#         for i in range(len( lis1)):
#             if lis1[i] != lis2[i]:
#              return f"Different, difference: {lis1[i]} and {lis2[i]}"
#         return "Same"
            
        
# a = [1,5,6,78,3]
# b = [1,5,6,78,32]
# print(check_lis(a,b))

'''SUM OF ALL ELEMENTS IN A LIST USING LAMBDA FUNCTION'''

# lis = [2,4,1,5,6]
# Sum = lambda : sum(lis)
# print(Sum())

'''OTP GENERATOR'''

# import random
# import time
# def func(a):
#      a = eval(input("Enter OTP here: "))
# otp = random.randrange(start=100000,stop=999999)
# print(f"Your OTP: {otp}")
# enter = eval(input("Enter OTP here: "))
# for i in range(1,4):
#             if enter != otp:
#              print("Wrong OTP")
#              func(enter)
# if enter == otp:
#     print("Varification completed")
# else:
#     print("wait for 25 seconds")
#     for j in range(0,26):
#           time.sleep(1)
#           print(f"{j:02d}",end='\r')

'''INSERTION SORT'''

# def insertionSort(a):
#     for i in range(1,len(a)):
#         curr = a[i]
#         prev = i-1
#         while prev >= 0 and a[prev] > curr:
#             a[prev+1] = a[prev]
#             prev -= 1
#         a[prev+1] = curr
#     for i in range(len(a)):
#         print(f"{a[i]}",end=" ")

# arr = [45,22,63,34,13,8]
# insertionSort(arr) 

'''FIBONACCI SERIES'''

def fib_series(n):
    if n <= 1:
        return n
    else:
        return (fib_series(n-1) + fib_series(n-2))
num = int(input("Enter a number: "))
for i in range(num):
    print(fib_series(i))    