# username = input("What is your name?: ")
# password = input("Enter your password: ")

# password_len = len(password)
# hidden_pass = "*" * password_len


# print(f"Hello {username}! Your password {hidden_pass} is {password_len} letters long.")

# my_list = [1,2,3,4,5,6,7,8,9,10]
# i = 0

# while i < len(my_list):
#     print(my_list)
#     i+=1


# for i in my_list:
#     num = i + 1
# print(num)


# for num in range(2):
#     print(list(range(10)))
# print("Hello World")

picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0], 
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

for row in picture:
    for pixel in row:
        if pixel == 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print("")


fill = "*"
empty = ""
for row in picture:
    for pixel in row:
        if pixel:
            print(fill, end = " ")
        else:
            print(empty, end = " ")
    print("")

duplicate = []
some_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in duplicate:
            duplicate.append(letter)

print(duplicate)