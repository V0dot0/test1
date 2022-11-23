# one two one two three two four three

sentence = input()
words = sentence.split(' ')
lst = []
result = {}
for word in words:
    result[word] = result.get(word, 0) + 1
    lst.append(result.get(word, 0) - 1)
print(str(lst).replace("[", "").replace("]", "").replace(",", ""))
