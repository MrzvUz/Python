my_name = "Ali"
your_name = input("Please, enter your name: ")

print(f"Hello {your_name}, my name is {my_name}.")

print()

# Converting user input to integer before printing the output.

age = int(input("Please, enter your age: "))
print(f"You have lived for {age * 12} months.")

# better way to make code readable

age = int(input("Please, enter your age: "))
months = age * 12
print(f"You have lived for {months} months.")
