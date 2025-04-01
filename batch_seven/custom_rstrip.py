# define a function that removes trailing whitespace from a string
def custom_rstrip_function(string):

    # initialize index to the last character's position
    index = len(string) - 1

    # loop while index is within bounds and character at index is a space
    while index >= 0 and string[index] == ' ':
        index -= 1
    
    # return substring without trailing spaces
    return string[:index + 1]

# get user input
string_name_input = input("Enter a string with trailing spaces: ")

# call the function with user input and print the result
print(custom_rstrip_function(string_name_input))