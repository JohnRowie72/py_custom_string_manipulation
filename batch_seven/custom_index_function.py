# define a function that returns the position at the first occurrence of the specified value.
def custom_index_function(string, substring):

    # loop through the string while checking for substring matches
    for index in range(len(string) - len(substring) + 1):
        # if substring is found, return the index
        if string[index:index + len(substring)] == substring:
            return index

    # if substring is not found, raise an error
# get user input for string
# get user input for substring
# try to call the function with user input and print the result