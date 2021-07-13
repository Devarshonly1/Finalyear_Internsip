#Exception Demo.
'''
--> well  try : & except :  are used to find out all the exception occurs while running programs.
      using it when can understand where And which place exception occured.
      And we developer can explain user where and what mistake he made during entering input.

--> while finally : is used to end this exception function so that program do not use unnecessary space.

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
