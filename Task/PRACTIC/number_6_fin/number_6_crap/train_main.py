import train_functions as tf

inpud: str = input("Имя файла \n")
txt1 = tf.readable(inpud)  # trainlog1.txt
#print (txt1) # посмотреть как преобразовался текст

inpud2: str = input("Куда сохранить \n")  # trainlog2.txt
txtsave = tf.transfer_save(txt1, inpud2)
print(txtsave)

# trainlog1.txt trainlog2.txt
