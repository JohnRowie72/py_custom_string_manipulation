# define a function that converts a string to uppercase
def custom_upper_function(string):

    # initialize an empty string to store the result
    result = ""

    # loop through each character in the input string
    for character in string:

        # if the character is lowercase, convert it to uppercase and append to result
        if 'a' <= character <= 'z':
            result += chr(ord(character) - 32)
        else:
            result += character

    # return the uppercase string
    return result

# get user input for string
string_name_input = input("Enter a string: ")

# call the function with user input and print the result
print(custom_upper_function(string_name_input))
