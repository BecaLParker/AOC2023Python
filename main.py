def first_instance_of_digit_word(line):
    digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    position = len(line) + 1
    first_digit_word = ''
    for digit_word in digit_words:
        if line.find(digit_word) < position and line.find(digit_word) != -1:
            position = line.find(digit_word)
            first_digit_word = digit_word
    return first_digit_word, position


def last_instance_of_digit_word(line):
    digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    end_position = 0
    last_digit_word = ''
    for digit_word in digit_words:
        if line.find(digit_word) + len(digit_word) - 1 > end_position:
            end_position = line.find(digit_word) + len(digit_word) - 1
            last_digit_word = digit_word
    return last_digit_word, end_position


def convert_to_digit(string):
    if string == 'one':
        return '1'
    elif string == 'two':
        return '2'
    elif string == 'three':
        return '3'
    elif string == 'four':
        return '4'
    elif string == 'five':
        return '5'
    elif string == 'six':
        return '6'
    elif string == 'seven':
        return '7'
    elif string == 'eight':
        return '8'
    elif string == 'nine':
        return '9'


def calibration_value(line):
    # Are there any digits in the line?
    if any(char.isdigit() for char in line):
        first_digit = next(filter(str.isdigit, line))
        first_digit_position = line.find(first_digit)
        last_digit = next(filter(str.isdigit, line[::-1]))
        last_digit_position = line.rfind(last_digit)
        if first_instance_of_digit_word(line)[1] < first_digit_position:
            first_digit = convert_to_digit(first_instance_of_digit_word(line)[0])
        if last_instance_of_digit_word(line)[1] > last_digit_position:
            last_digit = convert_to_digit(last_instance_of_digit_word(line)[0])
    else:  # There are no digits in the line
        first_digit = convert_to_digit(first_instance_of_digit_word(line)[0])
        last_digit = convert_to_digit(last_instance_of_digit_word(line)[0])

    print('first is ' + first_digit + ' and last is ' + last_digit)

    # concat the first and last digit and return as int
    return int(first_digit + last_digit)


def sum_calibration_values(lines):
    # initialize sum to 0
    sum = 0
    # loop through the lines
    for line in lines:
        # add the calibration value of each line to the sum
        sum += calibration_value(line)
    return sum


def get_lines_from_file(filepath):
    # open the file
    file = open(filepath, 'r')
    # read the lines from the file
    lines = file.readlines()
    # close the file
    file.close()
    # return the lines
    return lines

# print the sum of the calibration values of the lines in the file
#print(sum_calibration_values(get_lines_from_file('./inputs/day1.txt')))
