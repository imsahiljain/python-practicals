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

# 7 Check list is empty or not

if len(L) == 0:
    print("List of numbers is empty")
else:
    print("List of numbers is not empty")

if len(D) == 0:
    print("List of strings is empty")
else:
    print("List of strings is not empty")
