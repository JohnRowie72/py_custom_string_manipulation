# define a function that swaps the case of each character in a string
def custom_swapcase_function(string):

    # initialize an empty string to store the result
    result_of_string = ""

    # loop through each character in the input string
    for character in string:

        # if the character is uppercase, convert it to lowercase
        if 'A' <= character <= 'Z':
            result_of_string += chr(ord(character) + 32)

        # if the character is lowercase, convert it to uppercase
        elif 'a' <= character <= 'z':
            result_of_string += chr(ord(character) - 32)

        else:    
            # otherwise, leave it unchanged
            result_of_string += character

    # return the result string
    return result_of_string

# print the result of calling the function with the string "Hello, World!"
print(custom_swapcase_function("Hello, World!"))
