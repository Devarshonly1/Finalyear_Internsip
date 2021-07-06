# File Managment

"""

--> In file managment there are, WRITE ( w ) , READ ( r ) , APPEND ( a ) , WRITE + ( w+ ) , READ ( r+ )

"""

# WRITE ( w )

file=open("Demo1.txt","w")   # Here second " w " represent type of file. i.e. its Write only file.
file.write(" This file is written only function file, where user can only write in this file.")
file.close()

# READ ( r )

file=open("Demo1.txt","r")    # Here second " r " represent type of file. i.e. its Read only file.
print(file.read())
file.close()

# APPEND ( a )    # Here second " a " represent type of file. i.e. its Appends file. wich mean add new data in files.

file=open("Demo1.txt","a")
file.write("\nThis is an append function using which we can add new data in the existing file." )
file.close()

file=open("Demo1.txt","r")
print(file.read())
file.close()


# WRITE + ( w+ )   # Here second " w+ " represent type of file. i.e. its Write and read function file.

file=open("Demo2.txt","w+")
file.write(" This file is write and read function file, where user can  write and read this file.")
print(file.read())

"""
#Here we do not get any output as while writing it also go for reading file. and because of that your curser is at end.
#As we alread know that read function can only read any content in forward direction only.
"""

file.seek(0) #using this fuction we can shif the curser from end to any of the index number from where we want to read the file.
print(file.read())

print("Current curser position : ",file.tell()) # This function will help us to find curser position.



# READ+ ( r+ )   # Here second " r+ " represent type of file. i.e. its read and write function file.

file=open("Demo2.txt","r+")
file.write("This is read and write function file. opposite to the W+ file function.")
file.seek(0)
print(file.read())
file.close()
