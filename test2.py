import random
a = set()
# print(type(a))
n = int(input("kolvo mnozhestv"))
m = int(input("kolvo elementov mnozhestva"))
A = []
for i in range(n):
    A1 = []
    for j in range(m):
        A1.append(random.randint(-100,100))
    A.append(A1)
    print(A1)
B = []
for i in range(n):
    B1 = []
    for j in range(m):
        if A[i][j]%3 == 0:
            B1.append(A[i][j])
        B.append(B1)
    print(B1)
rest1 = set().union(A[0])
print(rest1)
rest = set().union(*B)
print(rest)
print(rest-rest1)
print(rest.difference(rest1))