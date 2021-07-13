# Prime file managment.

n=int(input("Enter N: "))

f=open("Demo4.txt","w")

for i in range (0,n+1) :
    f.write(str(i)+" ")
f.close()

f=open("Demo4.txt","r")
prime=open("prime.txt","w")

s=f.read().split(" ")[:-1]
for i in s:
    
    if int(i)>=2 :
        
        for j in range(2,int(int(i)/2)+1) :

            if int(i)%int(j)==0 :
                break
        else:
            prime.write(str(i)+" ")

f.close()
prime.close()
print("# Prime Numbers")
prime=open("prime.txt","r")
print(prime.read())
prime.close()            
