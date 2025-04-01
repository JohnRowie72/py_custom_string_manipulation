# define a function that pads a string with zeros to a specified width
def custom_zfill_function(string, width):

    # add zeros at the beginning if the string is shorter than the width
    return '0' * (width - len(string)) + string if len(string) < width else string

# get user input for string
string_name_input = input("Enter a string: ")

# get user input for width
width = int(input("Enter the width: "))

# call the function with user input and print the result
print(custom_zfill_function(string_name_input, width))
