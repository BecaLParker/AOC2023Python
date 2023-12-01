
def calibration_value(line):
    # convert input to string
    line = str(line)
    # get the first instance in the string which is a digit
    first = next(filter(str.isdigit, line))
    # get the last instance in the string which is a digit
    last = next(filter(str.isdigit, line[::-1]))
    # concat the first and last digit and return as int
    return int(first + last)
