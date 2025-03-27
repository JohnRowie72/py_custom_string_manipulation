# define a function that checks if all characters in a string are uppercase
def custom_isupper_function(string):

    # loop through each character in the input string
    for character in string:

        # if the character is not uppercase, return False
        if 'a' <= character <= 'z':
            return False

    # if no lowercase characters are found, return True
    return True

# print the result of calling the function with the string "HELLO WORLD"
print(custom_isupper_function("HELLO WORLD"))

# print the result of calling the function with the string "Hello World"
print(custom_isupper_function("Hello World"))
