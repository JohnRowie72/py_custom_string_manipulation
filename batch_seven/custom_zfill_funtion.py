# define a function that pads a string with zeros to a specified width
def custom_zfill_function(string, width):

    # add zeros at the beginning if the string is shorter than the width
    return '0' * (width - len(string)) + string if len(string) < width else string
    
# get user input for string
# get user input for width
# call the function with user input and print the result