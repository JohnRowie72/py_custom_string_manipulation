# define a function that removes a specified suffix from a string
def custom_removesuffix_function(string, suffix):

    # check if the string ends with the specified suffix
    if string.endswith(suffix):

        # return string without suffix
        return string[:-len(suffix)]

    # otherwise, return the original string
    return string

# get user input for string and suffix
string_name_input = input("Enter a string: ")
suffix = input("Enter a suffix to remove: ")

# call the function with user input and print the result
print(custom_removesuffix_function(string_name_input, suffix))
