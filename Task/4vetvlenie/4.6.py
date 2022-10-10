a = int(input())
a1= a//100
a2 = (a//10)%10
a3 = a%10
if (a1<a2) & (a2<a3) :
    print("DA")
else:
    print("NET")