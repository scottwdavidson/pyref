"""
Often, when dealing with iterators, we also need to keep a count of iterations. 
Python eases the programmers' task by providing a built-in function enumerate() for this task. 
The enumerate () method adds a counter to an iterable and returns it in the form of an 
enumerating object. This enumerated object can then be used directly for loops or converted 
into a list of tuples using the list() function.
"""

# Professional 
fruit = ["Apple", "Banana", "Plum", "Peach", "Grapefruit", "Grape"]
for index, element in enumerate(fruit):
    print(f"Element {element} is at index {index}")

fruit_enumeration = enumerate(fruit)
print(list(fruit_enumeration))

# note: once the enumeration has been iterated, it must be recreated
fruit_enumeration = enumerate(fruit)
for index, element in fruit_enumeration:
    print(f"Element {element} is at index {index}")

fruit_enumeration = enumerate(fruit)
index, element = next(fruit_enumeration)
print("---- using next() ----")
print(f"Element {element} is at index {index}")
index, element = next(fruit_enumeration)
print(f"Element {element} is at index {index}")
index, element = next(fruit_enumeration)
print(f"Element {element} is at index {index}")
