# Guess game.

import random 

n=int(input("Enter the range : "))
num=random.randint(1,n+1)

while True:

    Guess=int(input("Guess a number between the given range :"))

    if Guess==num :
        print(" You have guessed correct number " )
        break
    elif Guess>num :
        print(" You have guessed greater number ")
        
    elif Guess<num :
        print(" You have guessed smaller number")

    

    
