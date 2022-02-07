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

# 10 Take two lists and return True if they have atleast one common member

y = int(input("Now I want you to make one more string \nSo enter number of elements - "))
i = 0
A = []
while i < y:
    o = input("Enter a string - ")
    A.append(o)
    i += 1
print("Created new list of strings is - ", A)

i = 0
L = "False"
while i < len(D):
    p = 0
    while p < len(A):
        if D[i] == A[p]:
            L = "True"
        p += 1
    i += 1
print(L)
