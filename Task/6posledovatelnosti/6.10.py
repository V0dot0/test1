lst = input()
lst = 'ilunahamamheehtatata'
lst1 = list(lst)
lastPart = lst[::-1][0: lst1.index("h")+1]
lastPart = lastPart[::-1]
#print(lastPart)
firstPart = lst[0: lst1.index("h")]
#print(firstPart)
print (firstPart+lastPart)