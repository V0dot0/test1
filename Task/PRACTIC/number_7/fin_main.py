import fin_functions as fun

#print(fun.books_cvs_extract())

new_list = fun.get_name("Python")
print(str(new_list).title())

newer_list = fun.get_list(new_list)
print(newer_list)

newest_list = fun.get_totals(newer_list)
print(newest_list)

