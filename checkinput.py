#Write a function that takes two parameters: a prompt message and an error message.
#The function will prompt the user with the passed in prompt to enter an integer
#If the text entered cannot be cast to an int, display the error message.
#The function will continue to prompt the user to enter an integer until a proper integer is entered.
#The most direct way of doing this would be using a try block, which has not been covered yet. You will need to research this.
#Write supporting code to call the function, and then display the number that was entered.

def Ask_for_a_num():
    attempts = 0
    while True:    
        try:
            number = int(input("Enter a number: "))
        except:
            attempts += 1
            if attempts == 1:
                print("That ain't a number, fool.")
            elif attempts == 2:
                print("That still ain't a number.")
            elif attempts == 3:
                print("Come on. Just enter a number.")
            elif attempts == 4:
                pass
            elif attempts == 5:
                pass
            elif attempts == 6:
                pass
            elif attempts == 7:
                pass
            elif attempts == 8:
                pass
            elif attempts == 9:
                pass
            else:
                print("Screw it! I give up.")
                break
        else:
            print(f"You entered {number}.")
            break

Ask_for_a_num()