# define a function that removes a specific prefix from a string:
def custom_remove_prefix(string, prefix):
    
    # get the length of the prefix
    prefix_length = len(prefix)

    # check if the input string starts with the prefix
    if string[:prefix_length] == prefix:

        # if it does, return the substring after the prefix
        return string[prefix_length:]

    # otherwise, return the input string as is
    return string
    
# print the result of calling the function with the string "helloworld" and prefix "hello"