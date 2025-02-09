print("Welcome to unit converter")
a = '''
1. Feet ->
2. Inch ->
3. Centemeters ->'''
print(a)
n = int(input("Enter your choice:"))
if n == 1:
    feet_choice = '''
    1. Feet -> Inch
    2. Feet -> Centemeters
    3. Feet -> Meters
    4. Feet -> Miles'''
    print(feet_choice)
    n_feet = int(input("Enter an unit to convert from feet:"))
    if n_feet == 1:
        print("Feet -> inch")
        feet = eval(input("Enter a feet:"))
        inch = feet * 12
        print(feet,"feet =", inch,"inches")
elif n == 2:
    print("Inch -> Feet")
    inch = eval(input("Enter a value:"))
    feet = inch/12
    print(inch ,"inches =",feet,"feet")
elif n == 3:
    print("Centemeters")
    n_cm = int(input("Enter an unit to be converted:"))
    if n_cm == 1:    
        cm = eval(input("Enter a value"))
        print("Cm -> Inch")
        inch = cm * 0.3937
        print(cm, "cm =",inch,"inches")
    elif n_cm == 2:
        cm = eval(input("Enter a value"))
        print("Cm -> Feet")   
        feet = cm / 30.48
        print(cm,"cm =", feet,"feet")
mtr = eval(input("Enter a value"))
mile = eval(input("Enter a value"))
km = eval(input("Enter a value"))
