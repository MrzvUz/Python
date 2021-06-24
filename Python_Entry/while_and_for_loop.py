# is_learning = True

# while is_learning:
#     # print("You're learning")
#     user_input = input("Are you still learning?: ")
#     is_learning = user_input == "yes"


# user_input = input("Do you wish to run the program? (yes/no): ")

# while user_input == "yes":
#     print("We're running")
#     user_input = input("Do you wish to run the program again? (yes/no): ")

# print("We stopped running.")

# Exercise:

# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.
 
# Let's begin by asking the user to type either 'p' or 'q':
# user_input = input("Enter q or p: ")
 
# # Now we must repeat until they type 'q':
# while user_input != "q":
#     # Inside our loop, check if they typed 'p'. If they did, print "Hello"
#     if user_input == "p":
#         print("Hello")
#     # Now we must ask the user for their input again—otherwise we would be in an infinite loop!
#     user_input = input("Enter q or p: ")


#----------------------------------------------------------------#
# FOR LOOPS.

# friends = ["Bob", "Anne", "Rolf"]

# for friend in friends:
#     print(friend)

# for index in range(5, 10, 2):
#     print(index)


# students = (
#     {"name": "Rolf Smith", "grade": 90},
#     {"name": "Adam Wool", "grade": 78},
#     {"name": "Anne Run", "grade": 100},
#     {"name": "Jen Beauty", "grade": 80}
# )

# for student in students:
#     name = student["name"]
#     grade = student["grade"]

#     print(f"{name} has a grade of {grade}.")

double_numbers = [_ * 2 for _ in range(5)]
print(double_numbers)