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

"""
Filter:
Similar to map(), the filter() higher-order function takes a function and an iterable as inputs. 
The function in case needs to be of a Boolean nature, returning True/False values corresponding 
to the filter conditions. As output, it returns a subset of the input data that meets the 
conditions stipulated by the function. Its syntax is defined as follows:

filter(function, iterable)
"""

def only_castles(descriptor):
    CASTLE = "Castle"
    return descriptor[0:len(CASTLE)] == CASTLE

list_of_castles = list(filter(only_castles, list_of_photo_names))
print("---- filtered castles ----")
print(list_of_castles)
print(only_castles("Castle-A"))
