print("# List As Que")

from collections import deque

L=deque([])

# Inserting Numbers in List.

L.append(10)
print(list(L))
L.append(20)
print(list(L))
L.append(30)
print(list(L))
L.append(40)
print(list(L))
L.append(50)
print(list(L))
L.append(60)
print(list(L))

# Removing Nubers from List.

L.popleft()
print(list(L))
L.popleft()
print(list(L))
L.popleft()
print(list(L))
L.popleft()
print(list(L))
L.popleft()
print(list(L))
L.popleft()
print(list(L))
