# define a function that converts all characters of a string to lowercase
def custom_lowercase_function(string):

    # initialize an empty string to store the result
    result_of_string = ""

    # loop through each character in the input string
    for character in string:

        # if the character is uppercase, convert it to lowercase
        if 'A' <= character <= 'Z':
            result_of_string += chr(ord(character) + 32)
        else:
            # otherwise, leave it unchanged
            result_of_string += character

    # return the result string
    return result_of_string

# print the result of calling the function with the string "HeLLo, WoRLd!"
print(custom_lowercase_function("HeLLo, WoRLd!"))  # "hello, world!"
