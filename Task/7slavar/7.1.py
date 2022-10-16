sentence = input()
#sentence = 'ham tatata tratata help tam param param tam tam'
words = sentence.split(' ')
lst = []
result = {}
for word in words:
    result[word] = result.get(word, 0) + 1
    lst.append( result.get(word, 0) - 1)
print(lst)