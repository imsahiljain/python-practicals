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

# 6 Remove duplicates from a list

i = 0
while i < len(L):
    m = 0
    g = 0
    while g < len(L):
        if L[i] == L[g]:
            m += 1
            if m > 1:
                L.pop(i)
        g += 1
    i += 1
print("Number List with duplicates omitted - ", L)

i = 0
while i < len(D):
    m = 0
    g = 0
    while g < len(D):
        if D[i] == D[g]:
            m += 1
            if m > 1:
                D.pop(i)
        g += 1
    i += 1
print("String List with duplicates omitted - ", D)
