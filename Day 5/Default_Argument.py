# Default Argument.

"""
In Default argument, while runningparticular program
if user do not give any input then default input of argument is consider.

"""

def Class(a,b=2,c=12,d=4) :
    print("A:",a,"B:",b,"C:",c,"D:",d)


Class(100,200,300,400)
Class(10,30,60,40)
Class(a=4,d=40)
Class(a=27,b=7)
Class(a="DEVARSH")
Class(a="Parth",b=27)
