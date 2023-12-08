import unittest
import part1


class TestPartOne(unittest.TestCase):
    def test_case_one(self):
        self.assertEqual(part1.parse_calibration_value("1abc2"), 12)

    def test_case_two(self):
        self.assertEqual(part1.parse_calibration_value("pqr3stu8vwx"), 38)

    def test_case_three(self):
        self.assertEqual(part1.parse_calibration_value("a1b2c3d4e5f"), 15)

    def test_case_four(self):
        self.assertEqual(part1.parse_calibration_value("treb7uchet"), 77)

    def test_find_sum(self):
        data = [12, 38, 15, 77]
        self.assertEqual(part1.find_sum(data), 142)


if __name__ == "__main__":
    unittest.main()
