# define a function that left-justifies a string by adding it with spaces at the end
def custom_ljust_function(string, total_length):

    # calculate the number of spaces needed
    spaces_needed = total_length - len(string)

    # if spaces are needed, add them to the end of the string
    if spaces_needed > 0:
        return string + " " * spaces_needed

    # if the string is already long enough, return it as is
    return string
    
# print the result of calling the function with the string "hello" and width 10 
