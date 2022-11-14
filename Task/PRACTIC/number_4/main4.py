from Task.PRACTIC.number_4 import add4 as ad


requested_file = str(input("Enter the name of the file to read and return data: "))
returned_file = str(input("Enter the name of the file you want to write the data: "))
#     dataAf.txt
print(ad.read_file(requested_file))
ad.save_file(returned_file, requested_file)