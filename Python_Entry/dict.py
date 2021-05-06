# friend_ages = {
#     "Rolf": 24,
#     "Anne": 18,
#     "Jen": 20
# }
# print(friend_ages["Anne"])  # to get value of Anne.
# friend_ages["Bob"] = 26     # to add Bob to friend_ages dict.
# print(friend_ages)

# print()

# friends = (
#     {"name": "Rolf Smith", "age": 24},
#     {"name": "Adam Wool", "age": 30},
#     {"name": "Anne Run", "age": 18}
# )
# print(friends[0]["name"])
# print(friends[1]["name"])
# print(friends[2]["name"]) # or

# friends = friends[2]
# print(friends["name"]) # which is more readable.

# friends = ({"Rolf Smith", "age": 24})
# friends_ages = dict(friends)    # Use dict function to convert tuple in to dictionary.
# print(friend_ages)


# print()

# # Exaples:
# players = [
#     {
#         'name': 'Rolf',
#         'numbers': (13, 22, 3, 6, 9)
#     },
#     {
#         'name': 'John',
#         'numbers': (22, 3, 5, 7, 9)
#     }
# ]
# print(players[0]['numbers'])
# print(players[0]['numbers'][0])


# Exercise, Mu Solution.

# lottery_numbers = {13, 21, 22, 5, 8}


# """
# A player looks like this:

# {
#     'name': 'PLAYER_NAME',
#     'numbers': {1, 2, 3, 4, 5}
# }

# Define a list with two players (you can come up with their names and numbers).
# """

# players = [
#     {
#         "name": "Rolf", 
#         "numbers": {8, 21, 4, 22, 9}
#     },
#     {
#         "name": "Anne", 
#         "numbers": {13, 8, 2, 1, 11}
#     }
# ]

# name = players[0]["name"]
# numbers = players[0]["numbers"].intersection(lottery_numbers)
# print(f"Player {name} got {len(numbers)} right.")

# name = players[1]["name"]
# numbers = players[1]["numbers"].intersection(lottery_numbers)
# print(f"Player {name} got {len(numbers)} right.")

# """
# For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
# Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
# You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
# Then construct a string and print it out.

# Remember: the string must contain the player's name and the amount of numbers they got right!
# """


# # Course Solution.

# lottery_numbers = {13, 21, 22, 5, 8}
 
# """
# A player looks like this:
 
# {
#     'name': 'PLAYER_NAME',
#     'numbers': {1, 2, 3, 4, 5}
# }
 
# Define a list with two players (you can come up with their names and numbers).
# """
# players = [
#     {
#         "name": "Rolf",
#         "numbers": {1, 3, 8, 22, 21}
#     },
#     {
#         "name": "Jose",
#         "numbers": {4, 9, 10, 12, 15}
#     }
# ]
 
# # For each of the two players, print out a string like this: "Player PLAYER_NAME got 3 numbers right.".
# # Of course, replace PLAYER_NAME by their name, and the 3 by the amount of numbers they matched with lottery_numbers.
# # You'll have to access each player's name and numbers, and calculate the intersection of their numbers with lottery_numbers.
# # Then construct a string and print it out.
 
# # Remember: the string must contain the player's name and the amount of numbers they got right!
# name = players[0]["name"]
# numbers = players[0]["numbers"].intersection(lottery_numbers)
# print(f"Player {name} got {len(numbers)} numbers right.")
 
# name = players[1]["name"]
# numbers = players[1]["numbers"].intersection(lottery_numbers)
# print(f"Player {name} got {len(numbers)} numbers right.")



cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, STOP production")
        break   # Break function stops the loop.
    print(f"This car is {status}.")
    print("Shipping new car to the caustomer!")


cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars:
    if status == "faulty":
        print("Found faulty car, skipping..! Continue production")
        continue    # Continue function doesn't stop loop, it continues.
    print(f"This car is {status}.")
    print("Shipping new car to the caustomer!")