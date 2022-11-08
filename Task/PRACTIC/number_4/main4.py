from Task.PRACTIC.number_4 import add4 as ad

ad.read_file()
sv = ad.save_file('data.txt', ad.read_file())
count = sv[0]
words = sv[1]
words = ' '.join(words)
print(count,"=========================", words,sep = " \n")

text_to_write ="amount", count, "\n", words
new_text = open("dataAf.txt", mode='w+')
new_text.write(str(text_to_write))
#new_text.write(str(words))