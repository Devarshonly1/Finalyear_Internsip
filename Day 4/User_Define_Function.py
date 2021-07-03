
print("# User Defined Function in Python.")

#Function With No Argument & No Return Value.

def printLine() :
    print("*"*100)

printLine()
print("Wellcome to the world of python # User Define Function")
printLine()


#Function With Argument But NO Return Value.

def Multiply(x,y) :
    print("Multiply : ", x*y)
    
printLine()
a=int(input("Enter 1st  Value:"))
b=int(input("Enter 2nd Value:"))
Multiply(a,b)
printLine()

#Function With Argument & With Return Value

def Division(x,y) :
    return x/y

printLine()
x=int(input("Enter 1st  Value:"))
y=int(input("Enter 2nd Value:"))
print("Division : ", Division(x,y))
printLine()
