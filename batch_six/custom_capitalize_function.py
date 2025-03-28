# define a function that capitalizes the first character of a string and converts the rest to lowercase
def custom_capitalize_function(string):

    # if the string is empty, return it unchanged
    if not string:
        return string

    # convert the first letter to uppercase if it is lowercase
    first_character = string[0]
    if 'a' <= first_character <= 'z':
        first_character = chr(ord(first_character) - 32)

    # convert the rest of the letters to lowercase
    rest_of_string = string[1:].lower()

    # return the final capitalized string
    return first_character + rest_of_string
    
# print the result of calling the function with the string "hELLO, WORLD!"
