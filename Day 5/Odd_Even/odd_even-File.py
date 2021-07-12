# Odd / Even / Prime Number - FILE.

n=int(input("Enter N : "))

f1=open("Demo3.txt","w")

for i in range(1,n+1) :
    f1.write(str(i)+" ")
f1.close()

f1=open("Demo3.txt","r")

odd=open("odd.txt","w")
even=open("even.txt","w")

s=f1.read().split(" ") [:-1] 
for i in s :
    if int(i)%2==0 :
        even.write(i+" ")
    else :
        odd.write(i+" ")
        
odd.close()
even.close()
f1.close()

print("# Even File ")
even=open("even.txt","r")
print(even.read())
even.close()

print("# Odd File ")
odd=open("odd.txt","r")
print(odd.read())
odd.close()

