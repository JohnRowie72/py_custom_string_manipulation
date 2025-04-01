# define a function that checks if a string starts with a specified prefix
def custom_startswith_function(string, prefix):

    # check if the string starts with the specified prefix
    return string[:len(prefix)] == prefix
    
# get user input for string
# get user input for prefix
# call the function with user input and print the result