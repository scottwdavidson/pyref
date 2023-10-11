"""
Map : 
Being a higher-order function, the map function takes another function and an 
iterable (e.g., a list, set, tuple) as input, applies the function to the iterable, 
and returns a **MAP** object as output. Its syntax is defined as follows:

map(function, iterable)
"""
from datetime import date

# goal: append today's date to each photo name 
list_of_photo_names = ["Castle-A", "Castle-B", "Church-A", "Cathedral-X", "Statue-X"]
dated_list_of_photo_names = list(map(lambda photo_name: photo_name + '-2023-10-03', list_of_photo_names))
print(dated_list_of_photo_names)

def append_today_date(descriptor):
    return descriptor + "-" + str(date.today())
dated_list_of_photo_names = list(map(append_today_date, list_of_photo_names))
print(dated_list_of_photo_names)

