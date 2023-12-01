def calibration_value(line):
    # convert input to string
    line = str(line)
    # get the first instance in the string which is a digit
    first = next(filter(str.isdigit, line))
    # get the last instance in the string which is a digit
    last = next(filter(str.isdigit, line[::-1]))
    # concat the first and last digit and return as int
    return int(first + last)


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