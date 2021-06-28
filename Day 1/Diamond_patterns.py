# Diamomd pattern

n=int(input("Enter Range : "))


print(" # First Pattern ")

for i in range(1,n) :
    print(" * "*i)


print(" # Second Pattern ")

for i in range(1,n) :
    print(" "*(n-i),"*"*i)
    

print(" # Third Pattern ")

for i in range(1,n) :
      print(" "*(n-i)," *"*i,)


print(" # Forth Pattern ")

for i in range(n,0,-1) :
    print(" * "*i)


print(" # Fifth Pattern ")

for i in range(1,n) :
      print(" "*(n-i)," *"*i,)

for i in range(n,0,-1) :
    print(" "*(n-i), " *"*i)




