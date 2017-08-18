# Implementation of Edit-distance
def edit_distance(string_1, len_string1, string_2, len_string2):
    global matrix
    # Creates a list containing length of string1 lists, each of length of string2(all set to 0 initially)
    matrix = [[0 for j in range(len_string2+1)] for i in range(len_string1+1)]

    # '+1' is included in range, considering the case of empty string
    for i in range(len_string1+1):
        for j in range(len_string2+1):

            # if first string is empty then at least length of string2 elements need to be added
            if i == 0:
                matrix[i][j] = j

            # if second string is empty then at least length of string1 elements need to be dropped
            elif j == 0:
                matrix[i][j] = i

            # if element in both string are different, then there are three possiblites:
            # 1. Insert
            # 2. Delete
            # 3. Substitute
            elif string_1[i-1] != string_2[j-1]:
                # if insert results in less operation
                matrix[i][j] = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1]) + 1

            # if element in both string are same, then do nothing get the previous number of operations
            else:
                matrix[i][j] = matrix[i-1][j-1]
    return matrix[i][j]

string1 = raw_input("Enter First String: ")
string2 = raw_input("Enter Second String: ")
print "Minimum distance is: ", edit_distance(string1, len(string1), string2, len(string2))


# Function to print the alignment of the strings
def alignment(string_1, len_string_1, string_2, len_string_2):
    mod_string1 = string_1



alignment(string1, len(string1), string2, len(string2))
