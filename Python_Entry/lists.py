friends = ["Bob", "Anne", "Rolf"]
print(friends[2])


print()


friends = [["Bob", 30], ["Anne", 25], ["Rolf", 40]]
print(friends[2])
print(friends[2][0])


print()


friends = [
    ["Bob", 30],
    ["Anne", 25],
    ["Rolf", 40]
]
print(friends[2])
print(friends[2][0])


print()


friends = ["Bob", "Anne", "Rolf"]
friends.append("John")
print(friends)

friends.remove("John")
print(friends)


print()


friends = [
    ["Bob", 30],
    ["Anne", 25],
    ["Rolf", 40]
]

friends.append(["John", 45])
print(friends)

friends.remove(["John", 45])