# Lucky Draw.

import  random

L = [ ]
n=int(input("Enter the range : "))

for i in range (0,n+1) :
    L.append(i)
print("Numbers in the list :",L)

Draw=random.choice(L)
print("You win :",Draw)
L.remove(Draw)
 
while True :

    User=input("Would you like to continue :")

    if User == "yes" :
        Draw=random.choice(L)
        print("You win :",Draw)
        L.remove(Draw)
    

    elif User == " no":
         break
    
    else :
        print("The Remaining Numbers in Draw are: ",L)
