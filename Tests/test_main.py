from unittest import TestCase

from main import calibration_value, sum_calibration_values, get_lines_from_file, first_instance_of_digit_word, \
    last_instance_of_digit_word


class Test(TestCase):
    def test_first_instance_of_digit_word(self):
        assert first_instance_of_digit_word('two1nine') == ('two', 0)
        assert first_instance_of_digit_word('eightwothree') == ('eight', 0)
        assert first_instance_of_digit_word('abcone2threexyz') == ('one', 3)
        assert first_instance_of_digit_word('xtwone3four') == ('two', 1)
        assert first_instance_of_digit_word('4nineeightseven2') == ('nine', 1)
        assert first_instance_of_digit_word('zoneight234') == ('one', 1)
        assert first_instance_of_digit_word('7pqrstsixteen') == ('six', 6)

    def test_last_instance_of_digit_word(self):
        assert last_instance_of_digit_word('two1nine') == ('nine', 7)
        assert last_instance_of_digit_word('eightwothree') == ('three', 11)
        assert last_instance_of_digit_word('abcone2threexyz') == ('three', 11)
        assert last_instance_of_digit_word('xtwone3four') == ('four', 10)
        assert last_instance_of_digit_word('4nineeightseven2') == ('seven', 14)
        assert last_instance_of_digit_word('zoneight234') == ('eight', 7)
        assert last_instance_of_digit_word('7pqrstsixteen') == ('six', 8)

    def test_calibration_value(self):
        assert calibration_value('1abc2') == 12
        assert calibration_value('pqr3stu8vwx') == 38
        assert calibration_value('a1b2c3d4e5f') == 15
        assert calibration_value('treb7uchet') == 77
        assert calibration_value('two1nine') == 29
        assert calibration_value('eightwothree') == 83
        assert calibration_value('abcone2threexyz') == 13
        assert calibration_value('xtwone3four') == 24
        assert calibration_value('4nineeightseven2') == 42
        assert calibration_value('zoneight234') == 14
        assert calibration_value('7pqrstsixteen') == 76

    def test_sum_calibration_values(self):
        assert sum_calibration_values(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']) == 142
        assert sum_calibration_values(
            ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234',
             '7pqrstsixteen']) == 281

    def test_get_lines_from_file(self):
        assert get_lines_from_file('./test_input.txt') == ['this_is_a_test\n', 'AND ANOTHER TEST']



