from unittest import TestCase

from main import calibration_value, sum_calibration_values


class Test(TestCase):
    def test_calibration_value(self):
        assert calibration_value('1abc2') == 12
        assert calibration_value('pqr3stu8vwx') == 38
        assert calibration_value('a1b2c3d4e5f') == 15
        assert calibration_value('treb7uchet') == 77

    def test_sum_calibration_values(self):
        assert sum_calibration_values(['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']) == 142
