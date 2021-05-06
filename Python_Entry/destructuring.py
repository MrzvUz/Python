# # Destructuring such as taking the tuple and turining them into multiple variables.

# students = [
#     ("Rolf Smith", 90),
#     ("Adam Wool", 78),
#     ("Anne Run", 100),
#     ("Jen Beauty", 80)
# ]

# for name, age in students: # assigning multiple variables best practices.
#     # name = student["name"]    # not recomended
#     # grade = student["grade"]  # not recomended
#     print(name, age) # or even better way to print in next line:
#     print(f"{name} has a age of {age}.")


# # Assigning multiple variables.
# currencies = 0.8, 1.2
# usd,  eur = currencies
# print(usd, eur)


# students = {
#     "Rolf Smith": 90,
#     "Adam Wool": 78,
#     "Anne Run": 100,
#     "Jen Beauty": 80
# }

# for name in students:   # to get the keys of the dictionary.
#     print(name) 

# for ages in students.values(): # to get the values of the key in dict.
#     print(ages)

# for name, ages in students.items(): # to destructure two tuples name and ages.
#     print(f"{name} is {ages} years old.")

# Exercise FizzBuzz challenge:
'''
Print out numbers from 1 to 100 (including 100).
But, instead of printing multiples of 3, print "Fizz"
Instead of printing multiples of 5, print "Buzz"
Instead of printing multiples of both 3 and 5, print "FizzBuzz".
'''   
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)