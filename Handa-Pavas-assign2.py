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

            # if element in both string are different, then there are three possibilities:
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
print ("Enter strings in Uppercase !!!!")
string1 = raw_input("Enter First String: ")
string2 = raw_input("Enter Second String: ")
print 'OUTPUT 1: '
print "Minimum distance is: ", edit_distance(string1, len(string1), string2, len(string2))
print '\n'


# Function to print the alignment of the strings
def alignment(string_1, len_string_1, string_2, len_string_2):
    i = len_string_1-1
    j = len_string_2-1
    while i >= 0 and j >= 0:
        if string_1[i] == string_2[j]:
            i -= 1
            j -= 1
        else:
            row = i+1
            column = j+1
            values = [matrix[row][column-1],  # Insert
                      matrix[row-1][column],  # Delete
                      matrix[row-1][column-1]  # Substitute
                      ]
            index = values.index(min(values))
            # Insert
            if index == 0:
                # if position greater than length of string
                if i+1 >= len_string_1:
                    string_1 = string_1 + '*'
                else:
                    string_1 = string_1[:i+1] + '*' + string_1[i+1:]
                j -= 1
            # Delete
            elif index == 1:
                # if position greater than length of string
                if j+1 >= len_string_2:
                    string_2 = string_2 + '*'
                else:
                    string_2 = string_2[:j+1] + '*' + string_2[j+1:]
                i -= 1
            # Substitute (Nothing to insert in string)
            else:
                i -= 1
                j -= 1

    if i == -1 and j != -1:
        string_1 = ('*' * (j+1)) + string_1

    elif j == -1 and i != -1:
        string_2 = ('*' * (i + 1)) + string_2
    print 'OUTPUT 2:'
    print(string_1)
    length = len(string_1)
    print '|' * length
    print(string_2)

    i = 0
    opertion = ""
    while length != 0:
        if string_1[i] != string_2[i]:
            if string_1[i] != '*' and string_2[i] != '*':
                opertion += 's'
            elif string_1[i] == '*':
                opertion += 'i'
            else:
                opertion += 'd'
        else:
            opertion += ' '
        i += 1
        length -= 1
    print opertion


alignment(string1, len(string1), string2, len(string2))
