n = int(input("Enter number of elements you want to add in your list of numbers - "))
i = 0
L = []
while i < n:
    x = float(input("Enter a number - "))
    L.append(x)
    i += 1
print("Created list of Integers is - ", L)

# y = int(input("Enter number of elements you want to add in your list of strings - "))
# i = 0
# D = []
# while i < y:
#     z = input("Enter a string - ")
#     D.append(z)
#     i += 1
# print("Created list of strings is - ", D)

# 11 Print a new list after removing the 0th, 4th and 5th elements.
L2 = []
for x in range(len(L)):
    if x not in (0, 4, 5):
        L2.append(L[x])
print("New list after removing 0th, 4th and 5th elements is - ", L2)
