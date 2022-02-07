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

# 5 Count number of strings where string length is 2 or more and the first and last character are same

i = 0
M = 0
while i < len(D):
    if D[i][0] == D[i][-1] and len(D[i]) >= 2:
        M += 1
    i += 1
print("Number of strings where string length is 2 or more and the first and last character are same = ",  M)
