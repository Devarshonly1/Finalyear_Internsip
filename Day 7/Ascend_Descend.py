#ascending & descending


n=int(input("Enter the range:"))


def hastags() :
    print("# "*n)

hastags()

List=[ ]
for i in range (0,n+1) :
    List.append(i)

def original(List) :
    print("Original List :",List)


def Descend(List) :
     List.sort(reverse=True)
     print("Descending order :",List)
   
def Ascend(List) :
    List.sort()
    print("Ascending order :",List)

original(List)
hastags()
Ascend(List)
hastags()
Descend(List)








