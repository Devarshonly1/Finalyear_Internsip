#Calculator using User Define Function.

print("#CALCULATOR ")

def Star() :
    print("*"*100)

Star()

def add(x,y) :
    print("Addition : ", x+y)

def sub(x,y) :
    print("Substraction : ",x-y)

def Multiply(x,y) :
    print("Multiplication : ",x*y)
    
def Divide(x,y) :
    print("Division : ",x/y)

def Total(x,y) :
    print("Total : ", (x+y) + (x-y) + (x*y) + (x/y) )


a=int(input("Enter first Value : "))
b=int(input("Enter Second Value : "))

add(a,b)
sub(a,b)
Multiply(a,b)
Divide(a,b)
Total(a,b)


    
    

    
