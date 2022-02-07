L = []
i = 0
n = int(input("Enter the number of students you want to add"))

while i < n:
    x = input("Enter Name")
    L.append(x)
    i += 1
print("Formed list is ", L)

# 1 Display total number of characters present in the string

i = 0
while i < len(L):
    print("Number of characters in name of student ", i+1, " = ", len(L[i]))
    i += 1

# 2 Display Names beginning with 'a' or 'A'

i = 0
g = 1
while i < len(L):
    if L[i][0] == "a" or L[i][0] == "A":
        print("Name", g, " beginning with A or a - ", L[i])
        g += 1
    i += 1

# 3 Display Names ending with 'k' or 'K'

i = 0
g = 1
while i < len(L):
    if L[i][-1] == "k" or L[i][-1] == "K":
        print("Name", g, " ending with K or k - ", L[i])
        g += 1
    i += 1

# 4 Display Names ending with 'ing'

i = 0
g = 1
while i < len(L):
    if L[i][-3:] == "ing":
        print("Name", g, " ending with ing - ", L[i])
        g += 1
    i += 1

# 5 Display the 6th letter of each name

i = 0
g = 1
while i < len(L):
    print("6th letter of name ", g, " is - ", L[i][5])
    g += 1
    i += 1
