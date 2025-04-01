# define a function that finds the last occurrence of a substring in a string
def custom_rindex_function(string, substring):

    # loop through the string backwards while checking for substring matches
    for index in range(len(string) - len(substring), -1, -1):

        # if substring is found, return the index
        if string[index:index + len(substring)] == substring:
            return index

    # if substring is not found, raise an error
    raise ValueError(f"'{substring}' is not in the string")
    
# get user input for string
string_name_input = input("Enter a string: ")

# get user input for substring
substring = input("Enter a substring to find its last index: ")

# try to call the function with user input and print the result
try:
    print(custom_rindex_function(string_name_input, substring))
except ValueError as Error:
    print(Error)
