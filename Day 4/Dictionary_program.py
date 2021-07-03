# Dictionary and certain programs.

d={1: 'Tsunade', 2: 'Sai', 3: 'Sakura', 4: 'Kakashi', 5: 'Sasuke', 6: 'Naruto', 7: 'Itachi',8: 'Jiraya'}

print(d)

# Lets print all items in sequence.

for i in d:
    print(i," : ", d[i])
    
# Lets create a dictionary where each values is square of its keys.

n=int(input("Enter value of N : "))
d={ }

for i in range (1,n+1) :

   d[i]=i*i

print(d)



