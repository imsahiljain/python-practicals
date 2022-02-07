n = int(input("Enter number of elements you want to add in your list of numbers - "))
i = 0
L = []
while i < n:
    x = float(input("Enter a number - "))
    L.append(x)
    i += 1
print("Created list of Integers is - ", L)

y = int(input("Enter number of elements you want to add in your list of strings - "))
i = 0
D = []
while i < y:
    z = input("Enter a string - ")
    D.append(z)
    i += 1
print("Created list of strings is - ", D)

# 8 Clone or copy a list

k = int(input("Which list do you want to clone? \nType 1 for List of numbers \nType 2 for list of strings - "))

if k == 1:
    print("Original list - ", L)

    i = 0
    F = []
    while i < len(L):
        F.append(L[i])
        i += 1
    print("Cloned list - ", F)

elif k == 2:
    print("Original list - ", D)

    i = 0
    P = []
    while i < len(D):
        P.append(D[i])
        i += 1
    print("Cloned list - ", P)
