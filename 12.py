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

# 12 Print list after removing even numbers from it

i = 0
while i < len(L):
    if L[i] % 2:
        L.pop(i)
    i += 1
print("List of numbers after removing even numbers - ", L)
