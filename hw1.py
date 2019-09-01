# Shiyu Cheng, shiyucheng, 23329948


# Q1
# middle:(2 points) This function returns the middle element ofits only argument, which is assumed to be a three-element
# list.  RESTRICTION: Your solution must not contain any square brackets! ([and ]).

def middle(array):
    return array.pop(1)


def around(num):
    return num - 1, num, num + 1


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

def get_column(matrix, index, reverse = False):
    result = []
    for row in matrix:
        result.append(row[index])

    if (reverse == True):
        return result[::-1]
    else:
        return result

