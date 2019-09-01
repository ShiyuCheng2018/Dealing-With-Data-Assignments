# Shiyu Cheng, shiyucheng, 23329948


# Q1
# middle:(2 points) This function returns the middle element ofits only argument, which is assumed to be a three-element
# list.  RESTRICTION: Your solution must not contain any square brackets! ([and ]).

def middle(array):
    return array.pop(1)


def around(num, interval=1):
    return num - interval, num, num + interval


def second_biggest(array):
    if array[0] > array[1]:
        two_num = [array[0], array[1]]
    else:
        two_num = [array[1], array[0]]
    for num in array[2:]:
        if (two_num[0] > num) & (num > two_num[1]):
            two_num[1] = num
        elif two_num[0] < num:
            two_num[1] = two_num[0]
            two_num[0] = num
    return two_num[1]


def contains(matrix, value):
    for row in matrix:
        for each in row:
            if each == value:
                return True
    return False


def get_column(matrix, index, reverse=False):
    result = []
    for row in matrix:
        result.append(row[index])

    if reverse:
        return result[::-1]
    else:
        return result


def is_diagonal(matrix):
    for row in range(len(matrix)):
        for each in range(len(matrix[row])):
            if (row != each) & (matrix[row][each] != 0):
                return False
    return True


def is_upper_triangular(matrix):
    for row in range(len(matrix)):
        for each in range(len(matrix)):
            if (row > each) & (matrix[row][each] != 0):
                return False
    return True


def biggest(matrix):
    my_biggest = matrix[0][0]
    for row in matrix:
        for each in row:
            if my_biggest < each:
                my_biggest = each
    return my_biggest


def indices_biggest(matrix):
    my_biggest = biggest(matrix)
    my_list = []
    for row in range(len(matrix)):
        for each in range(len(matrix[row])):
            if my_biggest == matrix[row][each]:
                my_list.append((row, each))
    return my_list


def indices_divisible_by_3(matrix):
    result = []
    for row in range(len(matrix)):
        for each in range(len(matrix[row])):
            if (row + each) % 3 == 0:
                result.append(matrix[row][each])

    return result


def create_matrix(string):
    matrix = []
    get_row = string.split("/")
    for row in get_row:
        get_each = row.split(" ")
        column = []
        for each in get_each:
            if each != "":
                column.append(int(each))
        matrix.append(column)
    return matrix


def corners(matrix):
    return matrix[0][0], matrix[0][-1], matrix[-1][-1], matrix[-1][0]


def print_nzp(matrix):
    minus = ""
    body = ""
    for row in matrix:
        the_row = ""
        minus += "--"
        for each in row:
            if each < 0:
                the_row += " n"
            elif each == 0:
                the_row += " z"
            else:
                the_row += " p"
        body += "|" + the_row[1:] + "|\n"

    heads = "+" + minus[1:] + "+"
    return heads + "\n" + body[0:-1] + "\n" + heads


def sort_int_string(string):
    string_array = string.split()
    int_string = ""

    for each in string_array:
        if each == "":
            string_array.pop(string_array.index(each))

    for each in string_array:
        string_array[string_array.index(each)] = int(each)

    new = sorted(string_array)
    if new != []:
        for each in new[0:-1]:
            int_string += str(each) + " "
        int_string += str(new[-1])
    return int_string


def estimated_hours():
    return 2.5


def observation():
    return """
    I did not touch python over this summer, however, it dose not mean I did do any programming.
    I was focus on JavaScript on Web Development over this summer, so I pick Python really fast.
    These questions are generally fair for reviewing Python, but I did met a few problems while I 
    was completing them, luckily I solved them :) 
    Question: How deep that we gonna discover Python in this course? 
    """
