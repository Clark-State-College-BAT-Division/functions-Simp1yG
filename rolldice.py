#Write a function that takes as input number of dice and number of sides. The function will then return a list
#of randomly generated numbers in the proper count and range. For example if the the function is asked to generate
#3D6 or three sixed sided dice, then a potential output would be [2,2,6]
#This function cannot have any input or print statements.
#Write supporting code that will as the user for number of dice and sides, call the function, then report the results.
#The function should not be called if number of dice is zero or less and instead should report bad input to the user
#The function should not be called if number of sides is 1 or less and instead should report bad input to the user
#Sample outputs (your text does not have to match exactly)

# How many dice to roll? 3
# How many sides? 6
# Here are the results: [6, 1, 6]

# How many dice to roll? 0
# How many sides? 5
# Error: Sides must be greater than 1 and dice count greater than 0.

# How many dice to roll? 20
# How many sides? 20
# Here are the results: [18, 19, 6, 8, 13, 6, 6, 6, 18, 12, 20, 10, 14, 8, 14, 17, 12, 15, 20, 17]

def Dice_Town_Baby():
    import random
    while True:
        try:
            num_dice = int(input("How many dice to roll? "))
            if num_dice < 1:
                print("You have to roll at least one die.")
                continue
            break
        except:
            print("Please choose a number.")
    while True:
        try:
            num_sides = int(input("How many sides? "))
            if num_sides < 2:
                print("The number of sides must be greater than 1.")
                continue
            break
        except:
            print("Please choose a number.")
    rolls = []
    roll_total = 0
    for d in range(num_dice):
        dice_roll = random.randint(1, num_sides)
        roll_total = roll_total + dice_roll
        rolls.append(dice_roll)
    print(f"You rolled {rolls}\nfor a total of {roll_total}.")

Dice_Town_Baby()