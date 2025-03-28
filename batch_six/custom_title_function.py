# define a function that converts a string to title case
def custom_title_function(string):

    # split the string into words
    words = string.split()

    # initialize an empty string to store the result
    result_string = ""

    # loop through each word in the input string
    for word in words:

        # capitalize the first letter of the word
        first_character = word[0]
        if 'a' <= first_character <= 'z':
            first_character = chr(ord(first_character) - 32)

        # convert the rest of the letters to lowercase
        rest_of_word = word[1:].lower()

        # append the capitalized word to the result string
        result_string += first_character + rest_of_word + " "

    # return the result string with the trailing space removed
    return result_string.strip()
    
# print the result of calling the function with the string "hello WORLD from PYTHON!"