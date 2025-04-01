# define a function that checks if a string starts with a specified prefix
def custom_startswith_function(string, prefix):

    # check if the string starts with the specified prefix
    return string[:len(prefix)] == prefix

# get user input for string
string_name_input = input("Enter a string: ")

# get user input for prefix
prefix = input("Enter a prefix to check: ")

# call the function with user input and print the result
print(custom_startswith_function(string_name_input, prefix))
