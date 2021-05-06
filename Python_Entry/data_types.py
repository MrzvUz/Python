#---------------------------------------------------------------------------#
# Python has several built-in data type, that can be classed as:
'''
https://www.w3schools.com/python/python_datatypes.asp

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview

Examples:
x = "Hello World"	                            str	
x = 20	                                        int	
x = 20.5	                                    float	
x = 1j	                                        complex	
x = ["apple", "banana", "cherry"]	            list	
x = ("apple", "banana", "cherry")	            tuple	
x = range(6)	                                range	
x = {"name" : "John", "age" : 36}	            dict	
x = {"apple", "banana", "cherry"}	            set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	                                    bool	
x = b"Hello"	                                bytes	
x = bytearray(5)	                            bytearray	
x = memoryview(bytes(5))	                    memoryview
'''


# Fundamental Data Types
'''
int - integers
float - floating numbers
bool - Booleans represent one of two values: True or False.
str - strings
list - used to store multiple items in a single variable []
tuple - used to store multiple items in a single variable ()
set - used to store multiple items in a single variable {}
dict - Dictionaries are used to store data values in key:value pairs.
'''

# Classes - custom types

# Specialized Data Types

#---------------------------------------------------------------------------#
# Integers

# print(4)  # integer
# print(2 - 4)  # minus
# print(2 * 4)  # multiply
# print(4 / 2)  # devide
# print(2 ** 4)  # to the power of
# print(6 // 4)  # double devide round up the float to integer
# print(6 % 4)  # modulo gives the remainder of the division
# print(type(2 - 4))  # returns the type of the result
# print(type(4 / 6))

#---------------------------------------------------------------------------#
# Floats

# print(4 / 6)
# print(2 / 4)
# print(round(4 / 6))  # rounds up the float and returns integer
# print(abs(-20))  # returns absolute number of the value, means no negative numbers

#---------------------------------------------------------------------------#
# Operator Precedence
'''
1. ()     first executed numbers inside the brackets
2. **     second executed power of
3. * /    third executed multiply and devision
4. + -    forth executed plus or minus
'''

#---------------------------------------------------------------------------#
# Variables and best practices
'''
user_iq = 190         # snake case variable
user_age = iq / 4
_user_iq = 200        # private variable
__doc__               # dunder varible never should be changes
IQ = 250              # variable in capital letter mean it must NOT be changed
a,b,c = 1,2,3         # assigning multiple variables at the same time
'''


#---------------------------------------------------------------------------#
# Statement and Expression

# iq = 150              # whole line called statement
# user_age = iq / 4     # line after = sign is called expression

#---------------------------------------------------------------------------#
# Augmented assignment operator

# some_value = 5
# some_value = 5 + 2    # instead of doing 5 + 2 we can use augmented assignment operator
# some_value += 2       # shortened way of using += is called augmented assignment operator

#---------------------------------------------------------------------------#
# Strings

# print('hello world')
# print("hello world")
# long_string = '''
# W0W
# 0 0
# ===
# '''
# print(long_string)      # triple quoted called long string which allows to include multe line strings

#---------------------------------------------------------------------------#
# String Concatenation - which means joining two strings together

# print('hello' + ' world')

#---------------------------------------------------------------------------#
# Type Conversion

# print(type(str(100)))

#---------------------------------------------------------------------------#
# Escape Sequence

# weather = 'it's sunny'
# weather = "it's sunny"
# weather = "it's "kind of" sunny" # \ is escate sequence which recognizes the quites
# weather = "it\'s \"kind of\" sunny"
# \t    adds tab to the string
# \n    starts the string from new line

#---------------------------------------------------------------------------#
# Formatted strings

# name = 'Ahmad'
# age = 40
# print(f'Hello {name}! You are {age} years old.')    # best version is using f formated string
# print('Hello {}! You are {} years old.'.format('Ahmad', '40'))
# print('Hello {}! You are {} years old.'.format(name, age))
# print('Hello {1}! You are {0} years old.'.format(name, age))  # reverse the places of name with age

#---------------------------------------------------------------------------#
# String Indexes

# its = "me me me"
# num = "01234567"
# #   #  01234567
# print(its[0])
# print(num[5])

# # [start:stop]
# print(its[0:5])
# print(num[1:6])

# # [start:stop:stepover]
# print(its[0:5:2])
# print(num[1:6:2])

# # [start:]
# print(its[0:])
# print(num[1:])

# # [:stop]
# print(its[:5])
# print(num[:6])

# # [::stepover]
# print(its[::2])
# print(num[::2])

# # [::-stepover]
# print(its[::-1])  # reverses the stepover
# print(num[::-1])  # reverses the stepover

# print(its[-1])  # gets the last letter
# print(num[-1])  # gets the last number

#---------------------------------------------------------------------------#
# Built in Functions and String Methods

# https://docs.python.org/3/library/functions.html
# https://www.w3schools.com/python/python_ref_string.asp

# # functions - functions can come alone independently
# print(len('Akhmatali'))
# my_name = "Akhmatali"
# print(my_name[2:6])

# # methods - methods can't come alone, methods owned by something, variables whould come in front of methods
# quote = "to be or not to be"
# print(quote.upper())
# print(quote.capitalize())
# print(quote.lower())
# print(quote.find('not'))
# print(quote.replace('be', 'me'))

#---------------------------------------------------------------------------#
# Type Conversion Exercise
# birth_year = input('what your were you born?: ')
# age = 2021 - int(birth_year)
# print(f'You are {age} years old.')
