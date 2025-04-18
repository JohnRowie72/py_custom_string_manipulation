# define a function that counts the occurrences of a substring in a string
def custom_count_function(string, substring):

    # initialize count to 0
    count = 0

    # loop through the string while checking for substring matches
    for i in range(len(string) - len(substring) + 1):
        # if substring is found, increment count
        if string[i:i + len(substring)] == substring:
            count += 1
    
    # return the count of occurrences
    return count

# get user input for string
string_name_input = input("Enter a string: ")

# get user input for substring
substring = input("Enter a substring to count: ")

# call the function with user input and print the result
print(custom_count_function(string_name_input, substring))
