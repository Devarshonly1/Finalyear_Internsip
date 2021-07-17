# User Define Functions.


def MaxOfTwo(a,b):
        if a>b :
            print(a,": is Greater Number")
        else :
            print(b,": is Greater Number")

def MaxOfThree(x,y,z):
        if x>y :
            if x>z:
                print(x,": is Greater Number")
            else :
                print(z,": is Greater Number")
        
        elif y>z:
            print(y,": is Greater Number")
        else:
            print(z,": is Greater Number")
            


def Pattern(n):
    for i in range(1,n+1):
        print(" "*(n-i)," *"*i)

def OddEven(n):        
            if n%2==0:
                print(n,": Is Even Number")
            else :
                print(n,": Is Odd Number")

def Fibonacci(n):
    a,b=0,1
    while b<n:
        print(b," ")
        a,b=b,a+b

def Prime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0:
            print(n,": Is not a Prime Number")
            break
    else:
        print(n,": Is a Prime Number")

def Star(n):
        print(" * "*n)
        
