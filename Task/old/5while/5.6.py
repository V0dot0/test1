a1 = 1
a2 = 1
x = int(input())
i = 0
while i < x - 2:
    a3 = a1 + a2
    a1 = a2
    a2 = a3
    i += 1
print(i)