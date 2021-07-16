#Odd Even & Fibonacci using functions

n=int(input("Enter the range :"))

F1=open("File1.txt","w+")
print("F1 file is generated")

for i in range (0,n+1) :
    F1.write(str(i)+" ")

odd=open("odd.txt","w+")
even=open("even.txt","w+")

F1.seek(0)
x=F1.read().split(" ") [:-1]

def OddEven(n):
    for i in range(0,n+1):
        if i%2==0:
            even.write(str(int(i))+" ")            
        else:            
            odd.write(str(int(i))+" ")
           
OddEven(n)

print("# Even Numbers")
even.seek(0)
print(even.read())


print("# Odd Numbers")
odd.seek(0)
print(odd.read())

odd.close()
even.close()

Fibo=open("Fibonacci.txt","w")

def fibonacci(n):
    a,b=0,1
    while b<n:
        Fibo.write(str(b)+" ")
        a,b=b,a+b
        
fibonacci(n)

Fibo=open("Fibonacci.txt","r")
print("# Fibonacci Numbers")
print(Fibo.read())

Fibo.close()
F1.close()
