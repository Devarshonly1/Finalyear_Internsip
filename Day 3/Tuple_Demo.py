#Tuple Demo.

t=(10,200,30,1.1,2.2,3.3,"hello world",[200,400,600],True,False,True,"Python")

print(t)
print(t.count(200))
print(t.index(2.2))

for i in t :
    print(i)

print(t[7][1])

for i in t[7] :
    print(i)

t[7].pop()
print(t)

t[7].append(800)
print(t)


