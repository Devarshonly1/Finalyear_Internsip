# Random Number module
'''
--> In this we have to export random library using " import random "

'''
def star() :
    print(" * "*40)

import random
star()
print("Generate random number ")

print(random.randint(0,9999)) # In order to generate random number from particular range

star()

print("Choice any number from given range") # in order to chose any number from given list or in between any range 
n=int(input("Enter N :"))
L=[]
for i in range (0,n+1) :
    L.append(i)
    
print(random.choice(L))

star()
print("Guess number Game")
no=random.randint(1,20)
while True:

    guess=int(input("Guess a number between 1 & 20 :"))



    if guess==no :
        print("you guess CORRECT Number ")



    elif guess>no :
        print("you guessed BIGGER Number  ")



    elif guess<no :
        print("you guessed SMALLER Number ")

    else :

        break

