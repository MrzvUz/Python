# art_friends = {"Rolf", "Anne"}
# science_friends = {"Jen", "Charlie"}

# art_friends.add("Jen")
# print(art_friends)

'''Sets doesn't hold duplicates and it doesn't keep order.
Sets also used to remove duplicates in data. Also it is used
to check whether emelent exist in data.'''

# art_friends = {"Rolf", "Anne", "Jen"}
# science_friends = {"Jen", "Charlie"}

# art_but_bot_science = art_friends.difference(science_friends)
# science_but_bot_art = science_friends.difference(art_friends)
# print(art_but_bot_science)
# print(science_but_bot_art)

# not_in_both = art_friends.symmetric_difference(science_friends)
# print(not_in_both) # Members not in both.

# art_and_science = art_friends.intersection(science_friends)
# print(art_and_science) # Gives the elements which exists in both Sets.

# all_friends = art_friends.union(science_friends)
# print(all_friends) # Unites both sets and removes duplicates and returns all elements.

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
friend = input("Please, enter your friend's name if nearby: ")
# Add the name to the empty set
user_friends.add(friend)
# Print out the intersection between both sets. This gives us a set with those friends that are nearby.
user_friends.intersection(nearby_people)
print(user_friends)
