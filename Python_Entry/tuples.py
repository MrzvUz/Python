short_tuple = "Rolf", "Bob", "Anne"
a_bit_clearer = ("Rolf", "Bob", "Anne")
tuple_in_list = [("Rolf", "Bob", "Anne")]
not_a_tuple = "Rolf" # is not a tuple, it is just a list. Needs "Rolf", "Bob"

# Tuple immutable, you can't change. To add an element to tuple:
friends = ("Rolf", "Bob", "Anne")
friends = friends + ("John",)
print(friends) # Tuple did add "John", it created new tuple with "John included"

# In Lists you can add and remove elements but in Tuple you can not. You have to cretae new Tuple.