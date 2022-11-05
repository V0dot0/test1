#text = open('Words.txt')
#word_list = text.read().splitlines()
#word_list = [i.upper() for i in word_list]
#print(word_list)
#text.close()



a = int(input())

new_text = open("Record.txt", mode='r+')

new_text.seek(0)
found = int(new_text.read())
print("found num ", found)
if a > found:
    found = a


new_text.seek(0)
new_text.write(str(found))

#debug
new_text.seek(0)
fin = int(new_text.read())
print("final ", fin)

