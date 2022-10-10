a = 1
k = 0
prev = 9999
while a != 0:
    a = int(input())
    if prev < a:
        k += 1
    prev = a
print(k)