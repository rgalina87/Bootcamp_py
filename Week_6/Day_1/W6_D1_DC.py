# Get a string from the user. The user must provide a string that is 10 characters long.
user_string = input("Enter something: ")
user_string = int(user_string)
if (user_string) > 10:
    print('Warning! You can enter only 10 characters long')
elif (user_string) < 10:
    print('Warning! You can enter only 10 characters long')

# Inform the user what the first and last characters of the string are
if user_string[-1] == ''
	ptint('last character is')
elif user_string[0] == ''
	print('first character is')

# ‘Build’ the string up: print the first character, then the first 2, then the first 3, etc., until you print the entire string.
built_string = "Hello folks"
first_character = built_string[0]
print(first_character)
first_two = built_string[0:2]
print(first_two)
first_word = built_string[0:5]
print(first_word)

Swap some of the characters around, then print out this jumbled-up string to the user. Be sure to label it appropriately.
print (built_string.swapcase())
