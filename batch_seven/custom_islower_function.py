# define a function that checks if a string is lowercase
def custom_islower_function(string):

    # loop through each character in the string
    for character in string:

        # if any character is uppercase, return False
        if 'A' <= character <= 'Z':
            return False

    # if the loop completes, return True
    return True

# get user input for string
# call the function with user input and print the result
