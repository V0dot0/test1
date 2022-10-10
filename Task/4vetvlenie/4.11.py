a = int(input())
b = int(input())
c = int(input())
d = int(input())
a2 = a%2
b2 = b%2
c2 = c%2
d2 = d%2
a3=0
c3=0
# 0 black 1 white
if b2==1:
    if a2==0:
        print("chet-white")
        a3 = 1
    else:
        print("nechet-black")
        a3 = 0
if b2==0:
    if a2==1:
        print("chet-white")
        a3 = 1
    else:
        print("nechet-black")
        a3 = 0

if d2==1:
    if c2==0:
        print("chet-white")
        c3 = 1
    else:
        print("nechet-black")
        c3 = 0
if d2==0:
    if c2==1:
        print("chet-white")
        c3 = 1
    else:
        print("nechet-black")
        c3 = 0
if a3 == c3:
    print(" IS equal")
else:
    print(" NOT equal")
