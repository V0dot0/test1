a = 1
k = 1
max = -9999
prev = 9999
while a != 0:
    a = int(input())
    if prev == a:
        k += 1
    if prev != a:
        k = 1
    if k > max:
        max = k
    prev = a
print(max)