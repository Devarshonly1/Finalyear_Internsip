# Dictionary Functions.

d={1:"Devarsh",2:"Jaimil",3:"Ayush",4:"Abhi",5:"Smit",6:"Nirav",7:"Ram",8:"Meet",9:"Harry",10:"Jack"}

print(d)
print(d.get(7))
print(d.items())
print(d[1],d[10],d[3])
print(d.values())
print(d.keys())
d.pop(7)         # In dictionary we are supposed to give arguments while using pop function.
print(d)
d.popitem()  # or else use "popitem()" function to remove last value with its key i.e entire element
print(d)
# Inorder to add new value and key use below method or function

d[12]="Black pearl" # This will Add new item at the end of dictionary
print(d)

d1={10:"Naruto",11:"Jiraya"} # or else create a new dictionar and attached it behind original one
d.update(d1)                          #just like extend function of list
print(d)



