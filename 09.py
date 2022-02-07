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

# 9 List of words that are longer than 'n' from a list of words

num = int(input("Enter number for which you want to check length of words - "))

i = 0
Q = []
while i < len(D):
    if len(D[i]) > num:
        Q.append(D[i])
    i += 1

print("Words longer than ", num, " letters are - ", Q)
