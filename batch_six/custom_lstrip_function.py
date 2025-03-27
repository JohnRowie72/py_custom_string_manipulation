# define a function that removes leading spaces from a string
def custom_lstrip(string):

    # start from the beginning of the string
    index = 0

    # loop until a non-space character is found
    while index < len(string) and string[index] == " ":
        index += 1

    # return the substring starting from the non-space character
    return string[index:]
    
# print the result of calling the function with the string "   hello"
print(custom_lstrip("   hello"))  # "hello"
