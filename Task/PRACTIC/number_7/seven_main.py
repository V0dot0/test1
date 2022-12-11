import seven_functions as fun
#
fun.csv_to_txt_service()
#
matches = fun.get_books("Python")
print(matches)
#
print(fun.get_totals(matches))