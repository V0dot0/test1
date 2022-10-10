a = int(input())
b = int(input())
c = int(input())
n = 0
if (a==b):
    n+=1
if (a==c):
    n += 1
if (b==c):
    n+=1
if (n == 1):
    n+=1
print(n)