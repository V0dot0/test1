lst = input()
#lst = 'ilumahABRIKOShamABRICOShtata'
lst1 = list(lst)
firstPart = lst[lst1.index("h")+1: -1]
print(firstPart)
lastPart = lst[::-1][1: lst1.index("h")]
lastPart = lastPart[::-1]
print(lastPart)
finalPart = firstPart.replace(lastPart," ")
print(finalPart)
