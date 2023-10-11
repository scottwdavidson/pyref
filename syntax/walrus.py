""" 
The walrus operator, i.e., := , streamlines assignment and value check 
"""

def some_expensive_calculation():
    print("expensive calculating happening ... ")
    return 25

# Novice approach
value = some_expensive_calculation()
if value > 10:
    print(value)

# Professional approach
if (value := some_expensive_calculation()) > 10:
    print(value)