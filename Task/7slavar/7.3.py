slavar = {
          'joe':5,
            'daun':6,
            'joe':2}
#slavar = {}
Hidden = []
#number = int(input(" Введите число: "))
#while number != 0:
    #key = input(" Введите президента: ")
    #value = int(input(" Введите его голоса : "))
    #slavar[key] = value
    #Hidden.append(key)
    #number -= 1
for name in range(slavar):
    slavar[name] = slavar.get(name, 0) + 1
print(slavar)
#print(Hidden)

#for word in phone_book:
 #   result[word] = result.get(word, 0) + 1
 #   result2.append( result.get(word, 0) - 1)
#print(result2)

#men = int(input())
#men_works = {}
#for _ in range(men):
#    name = input()
 #   men_works[name] = men_works.get(name,0)+1
#print(sum((i for i in men_works.values() if i >1)))
