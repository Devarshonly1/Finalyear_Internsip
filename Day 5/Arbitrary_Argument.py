#Arbitrary Argument.

def demo(a,b,c,*d,**e) :
    print("A:",a,"B:",b,"C:",c,"D",list(d),"E",e)

demo(1,2,3,4,5,6,7,8,9,10,11,12,A=100,B=200,C=300,D="Devarsh",E="Black Pearl")
demo(10,20,30,40,50,60,X="Naruto",Y="Tsunade",Z="Devarsh")

"""
--> Well using Star " * " we can make any argument into Arbitarry argument where it can take infinite inputs.
      But it should compulsary start from RIGHT to LEFT.Also we can skip any argument between. if it happen then it will wont work.
      But it will apear in tuple so inorder to perform function on it we have to convert it into list  

-->While using double star " ** " we can call ditionary.

      """
