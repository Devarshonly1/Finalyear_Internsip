#Exception Demo.
'''
--> well  try : & except :  are used to find out all the exception occurs while running programs.
      using it when can understand where And which place exception occured.
      And we developer can explain user where and what mistake he made during entering input.

--> while finally : is used to end this exception function so that program do not use unnecessary space.
     .aslo while working on file and data base function where we need to close certain file after its work is done
     then we should close them inside " finally : " function , as we know that finally will always called irrespective of any exception.


'''
    
a=("Hello World of  Python")
try:
    b=int(input("Enter Value of  b : "))
    c=int(input("Enter value of  c : "))

    d=b+c
    e=b*c
    f=b/c
    g=b-c

    print(a)
    print("Addition : ", d )
    print( "Multiplication : ", e  )
    print("Division : ", f  )
    print( "Substraction :", g )

except Exception as x:
    print("Exception caught :", x)

finally:
    print("Finally called")
