# my_number = 99
# user_number = int(input("Enter a number: "))

# matches = my_number == user_number
# if user_number ==  my_number:
#     print(f"You got it right. It's: {matches}")
# else:
#     print(f"Please, try again. It's: {matches}")
# print(f"Thank you for your time!")


# print()


# age = int(input("Enter your age: "))
# can_learn_programming = age > 0 and age < 150

# print(f"You can learn programming: {can_learn_programming}.")


# print()


# age = int(input("Enter your age: "))
# usually_working = age >= 18 and <=65

# print(f"At {age}, you are usually working: {usually_working}.")

# if:
# x = True and False
# print(x) # with "and" if it is False it gives the 2nd value which is False

# X = True or False
# print(x) # with "or" it is oposite. If it is True it gives the 1st value which is False.

# name = input("Enter your first name: ")
# surname = input("Enter you surname: ")

# greeting = name or f"Mr. {surname}"
# print(greeting)

# print()

# print(not 35) # "not" always gives the opposite value of the actual value.


# print()


# age = int(input("Enter your age: "))
# side_job = True
# print(age > 18 and age < 65 or side_job)

# print()

friends = ["Rolf", "Bob", "Anne"]
family = ["Jen", "Charlie"]

user_name = input("Please, enter your name: ")

if user_name in friends:
    print(f"Hello, my friend {user_name}!")
elif user_name in family:
    print(f"Hello, my relative {user_name}!")
else:
    print(f"Sorry, {user_name}, I don't know you.")