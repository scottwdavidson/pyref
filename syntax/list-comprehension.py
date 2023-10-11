""" 
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
"""

# Novice - build list of squared numbers 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)
print(squared_numbers)

# Professional - build list of squared EVEN numbers 
squared_even_numbers = [num ** 2 for num in numbers if num % 2 == 0]
print(squared_even_numbers)
