


# the game Computeer picks a random number(secret) between 1 to 100 and the 
# we take one number(guess) input from the user and checks if 
# he chose the correct number as of the computer or not and 
# we also count how many attempts he make 




# 1 Number game  


import random

def play_game() :

    secret = random.randint(1,100)
    attempt =0 

    print("---New game---")
    print("I'm thinking a number between 1 to 100 :")


    while True:

        try:

            choice = int(input("Enter your Choice :"))
        except ValueError :
            print("Enter a Valid number ")
            continue 
        
        attempt+=1 

        if(choice==secret):
            if(attempt<=5):
                print("CORRECT !")
                print("Raating : Amazing !")
            elif(attempt<=8):
                print("CORRECT !")
                print("Rating : Good job")

            else:
                print("CORRECT !")
                print("Raitng : Keep practicing!")

            break


        elif(choice<secret):
            print("A bit HIGHER , try again")

        else:
            print("A bit LOWER , try again")



print("Welcome to the NUMBER GAME !")

while True:

    play_game()

    again = input("Play again? (yes/no) :")

    if again.lower() != "yes" :
        print("see you again ")
        break 









