def first_last(array):
    return array[0], array[-1]


def dups_dict(me_dict):
    values = []
    for row in me_dict.values():
        for each in row:
            values.append(each)
    if len(values) == len(list(set(values))):
        return False
    else:
        return True


def substr_in_values(my_dict, string):
    result_keys = []
    for key in my_dict.keys():
        for value in my_dict[key]:
            if string.upper() in value.upper():
                result_keys.append(key)
                continue
    return sorted(list(set(result_keys)))


def count_lets(str, all=False):
    result_all = []
    result = []

    for each_char in range(97, 123):
        char = chr(each_char)
        count = 0
        for each_str in str:
            if each_str.lower() == char:
                count = count + 1
        if count > 0:
            result.append(count)
            result.append(char)
        result_all.append(count)
        result_all.append(char)

    if all:
        return result_all
    else:
        return result


def print_index(text):
    p = open(text)
    o = open(text)
    read = o.readlines()
    head = ""
    uniques = sorted(list(set(p.read().split())))
    head += str(len(uniques)) + " unique words: " + ", ".join(uniques)
    string = head + "\n\n"

    for unique in uniques:
        each_string = unique + " : "
        for line in range(len(read)):
            if unique in read[line].split():
                each_string += str(line + 1) + ", "
        string += each_string[:-2] + "\n"

    p.close()
    o.close()

    print(string[:-1])


def four_lines():
    capital = chr(65)
    small = chr(97)
    sign = chr(33)
    num = chr(48)
    for i in range(65, 91):
        capital += chr(i)
    for i in range(97, 123):
        small += chr(i)
    for i in range(33, 48):
        sign += chr(i)
    for i in range(48, 58):
        num += chr(i)

    print(capital[1:])
    print(small[1:])
    print(num[1:])
    print(sign[1:])


four_lines()


def cp_range(string):
    cp = []

    for each in string:
        cp.append(ord(each))

    return sorted(cp)[0], sorted(cp)[-1]


def mystry(array):
    string = ""
    for each in array:
        print(each)
        string += chr(each[0]) * each[1]


def binhex(num):
    first = ""
    second = ""
    bin_string = format(num, 'b')

    if len(bin_string) % 4 == 1:
        bin_array = bin_four("000" + bin_string)
    elif len(bin_string) % 4 == 2:
        bin_array = bin_four("00" + bin_string)
    elif len(bin_string) % 4 == 3:
        bin_array = bin_four("0" + bin_string)
    else:
        bin_array = bin_four(bin_string)

    for each in bin_array:
        second += f"{int(each, 2):4X}" + " "

    for each in bin_array:
        first += each + " "

    return first[:-1] + "\n" + second[:-1]


# bin_four is a function that pass a bin string
# (ex: 01111101), and return an array ['0111', '1101']
def bin_four(string):
    bin_array = []
    for each in range(len(string) // 4):
        bin_array.append(string[0 + each * 4: 4 + each * 4])
    return bin_array


def my_int(string, base=10):
    isNeg = False

    if string[0] == "-":
        len_str = len(string) - 1
        my_str = string[1:]
        isNeg = True
    else:
        len_str = len(string)
        my_str = string

    if base != 1:
        num = 0
        for i in range(len_str):
            num += digit_val(my_str[len_str - i - 1]) * (base ** i)
    else:
        num = len_str

    if isNeg:
        return -num
    else:
        return num


def digit_val(string):
    if 65 <= ord(string) <= 90:
        return ord(string) - 65 + 10
    elif 97 <= ord(string) <= 122:
        return ord(string) - 97 + 10

    return ord(string) - ord("0")


def estimated_hours():
    return 2.5


def observations():
    return """
    I did not touch python over this summer, however, it dose not mean I did do any programming.
    I was focus on JavaScript on Web Development over this summer, so I pick Python really fast.
    These questions are generally fair for reviewing Python, but I did met a few problems while I 
    was completing them, luckily I solved them :) 
    Question: How deep that we gonna discover Python in this course? 
    """
