from Task.PRACTIC.number_4 import add4 as ad

ad.read_file()
sv = ad.save_file('data.txt', ad.read_file())
count = sv[0]
words = sv[1]
words = ' '.join(words)
words = words.replace(" ", "\n")
print(count, words)


text_to_write = count, words
new_text = open("dataAf.txt", mode='w+')
new_text.write(str(count))
new_text.write(str("\n============\n"))
new_text.write(str(words))