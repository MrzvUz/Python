splitString = "Thsi string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedSting = "1\t2\t3\t4\t5"
print(tabbedSting)

print('The pet shop owner said "No, no, \'e\'s uh, ...he\'s resting."')
# or
print("The pet shop owner said \"No, no, 'e' uh, ... he's resting\".")

print("""The pet shop owner said "No, no, 'e's uh, ...he's resting". """)


anotherSplitString = """This string has been
splip over
to several
lines"""
print(anotherSplitString)


anotherSplitString = """This string has been \
splip over \
to several \
lines."""
print(anotherSplitString)


# Exercise
print("Number 1\tThe Larch")
print("Number 2\tThe Horse Chestnut")

# print("C:\Users\timbuchalka\notes.txt") # causes an error beacuse of backslash and t + n
# first solution is to include row string "r" befor ""
print(r"C:\Users\timbuchalka\notes.txt")
# second solution is using double back slashes.
print("C:\\Users\\timbuchalka\\notes.txt")
