# define a function that centers a string by adding spaces on both sides
def custpm_center_function(string, total_length):

    # calculate the total number of spaces needed
    total_spaces = total_length - len(string)

    # determine how many spaces are needed on each side
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces

    # create the centered string
    return " " * left_spaces + string + " " * right_spaces
    
# print the result of calling the function with the string "hello" and length 11
