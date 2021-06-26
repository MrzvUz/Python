# def checkDriverAge():
#     age = input("What is your age?: ")

#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge()

# def test(a):
#     return a * 2
# print(test(4))


# def say_hello(name, role):
#     return f"Hello {name}! How is your {role} career is going?"

# print(say_hello("Ali", "DevOps"))




# def highest_even(li):
#     even_hi_num = []
#     for num in li:
#         if num % 2 == 0:
#             even_hi_num.append(num)
#     return max(even_hi_num)
# print(highest_even([10, 2, 3, 4, 5, 6, 8, 10]))


#Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat("Jimmy", 10)
# cat2 = Cat("Timmy", 15)
# cat3 = Cat("Pimmy", 18)

# # 2 Create a function that finds the oldest cat
# def oldest_cat(*args):
#     return max(args)
# print(f"The oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old.")


# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # Instantiate the Cat object with 3 cats
# peanut = Cat("Peanut", 3)
# garfield = Cat("Garfield", 5)
# snickers = Cat("Snickers", 1)


# # Find the oldest cat
# def get_oldest_cat(*args):
#     return max(args)


# # Output
# print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")


# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #1 Add nother Cat

# class Jimmy(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = []




# #3 Instantiate the Pet class with all your cats use variable my_pets
# cat_Simon = Simon("I'm Simon", 10)
# cat_Sally = Sally("I'm Sally", 15)
# cat_Jimmy = Jimmy("I'm Jimmy", 20)
# # def Cat(**kwargs):
# #     my_cats.append(kwargs)


# #4 Output all of the cats walking using the my_pets instance

# print(f"{cat_Simon.walk(), cat_Sally.walk(), cat_Jimmy.walk()}")

### Solution

# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #1 Add nother Cat
# class Suzy(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [Simon('Simon', 4), Sally('Sally', 21), Suzy('Suzy', 1)]

# #3 Instantiate the Pet class with all your cats
# my_pets = Pets(my_cats)

# #4 Output all of the cats singing using the my_pets instance
# my_pets.walk()

# my_student = {
#     "name": "Rolf Smith",
#     "grades": [70, 88, 90, 99]
# }

# def average(student):
#     return sum(student["grades"]) / len(student["grades"])
# print(average(my_student))



# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#         n = float(user_input)
#     except ValueError:
#         print('Your input was invalid.')
#     finally:
#         n_square = n ** 2
#         return n_square
# print(power_of_two())

def interact():
    while True:
        try:
            user_input = int(input('Please input an integer:'))     # try to turn user input into an integer
        except ValueError:
            print('Please input integers only.')  # print a message if user didn't input an integer
        else:
            print('{} is {}.'.format(user_input, 'even' if user_input % 2 == 0 else 'odd'))     # print even/odd if the user input an integer
        finally:    # regardless of the previous input being valid or not
            user_input = input('Do you want to play again? (y/N):')     # ask if the user wants to play again
            if user_input != 'y':       # quit if the user didn't input `y`
                print('Goodbye.')
                break   # break the while loop to quit