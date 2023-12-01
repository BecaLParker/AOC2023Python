
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
