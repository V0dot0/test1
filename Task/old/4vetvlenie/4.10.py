a = int(input())
b = int(input())
a2 = a%2
b2 = b%2

if b2==1:
    if a2==0:
        print("chet-white")
    else:
        print("nechet-black")
if b2==0:
    if a2==1:
        print("chet-white")
    else:
        print("nechet-black")
