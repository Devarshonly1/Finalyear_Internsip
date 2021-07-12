#ascending & descending

import random

n=int(input("Enter the range:"))

def hastags() :
    print("# "*n)

hastags()

List=[ ]
for i in range (0,n+1) :
    List.append(i)

def function(List) :
    print("Entire List",List)

function(List)

hastags()

List.sort(reverse=True)
print("Descending order :",List)

hastags()

List.sort()
print("Ascending order :",List)










