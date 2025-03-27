# define a function that checks if a string ends with a specific suffix
def custom_endswith_function(string, suffix):

    # get the length of the suffix
    suffix_length = len(suffix)

    # remove the last 'suffix_length' characters from the input string
    remove_last_suffix = string[-suffix_length:]

    # compare the removed part with the suffix and return the result
    return remove_last_suffix == suffix

# print the result of calling the function with the string "hello world" and suffix "world"
print(custom_endswith_function("hello world", "world"))

# print the result of calling the function with the string "hello world" and suffix "hello"
print(custom_endswith_function("hello world", "hello"))