#text = open('Words.txt')
#word_list = text.read().splitlines()
#word_list = [i.upper() for i in word_list]
#print(word_list)
#text.close()


a = int(input())
b = 3
new_text = open("Record.txt", mode='r+')
if a>b :
    b = a
new_text.seek(0)
print(new_text.read())
new_text.seek(0)
new_text.write(str(b))
print(new_text.read() + 2)