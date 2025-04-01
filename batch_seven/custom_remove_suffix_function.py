# define a function that removes a specified suffix from a string
def custom_removesuffix_function(string, suffix):

    # check if the string ends with the specified suffix
    if string.endswith(suffix):

        # return string without suffix
        return string[:-len(suffix)]

    # otherwise, return the original string
    return string
    
# get user input for string and suffix
# call the function with user input and print the result  