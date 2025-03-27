# define a function that removes leading spaces from a string
def custom_lstrip(string):

    # start from the beginning of the string
    i = 0

    # loop until a non-space character is found
    while i < len(string) and string[i] == " ":
        i += 1

    # return the substring starting from the non-space character
    return string[i:]
    
# print the result of calling the function with the string "   hello"