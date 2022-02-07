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

# 4 Smallest number

i = 0
M = 0
while i < len(L):
    M = L[0]
    if L[i] < M:
        M = L[i]
    else:
        M = L[0]
    i += 1
print("Smallest number = ", M)
