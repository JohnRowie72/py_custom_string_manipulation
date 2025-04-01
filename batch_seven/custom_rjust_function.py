# define a function that right-justifies a string to a specified width
def custom_rjust_function(string, width, fill_character=' '):

    # add spaces at the beginning if the string is shorter than the width
    return fill_character * (width - len(string)) + string if len(string) < width else string

# get user input for string
string_name_input = input("Enter a string: ")

# get user input for width
width = int(input("Enter the width: "))

# call the function with user input and print the result
print(custom_rjust_function(string_name_input, width))
