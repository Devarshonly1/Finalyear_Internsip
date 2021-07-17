import UDF

while True:

    print("1 : MaxOfTwo")
    print("2 : MaxOfThree")
    print("3 : Pattern")
    print("4 : OddEven")
    print("5 : Fibonacci")
    print("6 : Prime")
    print("7 : Star")
    print("8 : Exit")

    num=int(input("Enter your choice: "))

    if num==1:
        a=int(input("Enter first value :"))
        b=int(input("Enter second value :"))
        UDF.MaxOfTwo(a,b)

    elif num==2:
        x=int(input("Enter first value :"))
        y=int(input("Enter second value :"))
        z=int(input("Enter third value :"))
        UDF.MaxOfThree(x,y,z)

    elif num==3:
        n=int(input("Enter N :"))
        UDF.Pattern(n)

    elif num==4:
        n=int(input("Enter N :"))
        UDF.OddEven(n)

    elif num==5:
        n=int(input("Enter N :"))
        UDF.Fibonacci(n)

    elif num==6:
        n=int(input("Enter N :"))
        UDF.Prime(n)

    elif num==7:
        n=int(input("Enter N :"))
        UDF.Star(n)

    elif num==8:
        break

    else :
        continue
        
