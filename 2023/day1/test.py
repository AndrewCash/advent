import unittest
import part1
import part2


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


class TestPartTwo(unittest.TestCase):
    def test_correct_calibration_case_one(self):
        value = part2.correct_calibration_value("two1nine")
        self.assertEqual(value, 219)

    def test_parse_calibration_case_one(self):
        value = part2.parse_calibration_value("219")
        self.assertEqual(value, 29)

    def test_correct_calibration_case_two(self):
        value = part2.correct_calibration_value("eightwothree")
        self.assertEqual(value, 823)

    def test_parse_calibration_case_two(self):
        value = part2.parse_calibration_value("823")
        self.assertEqual(value, 83)

    def test_correct_calibration_case_three(self):
        value = part2.correct_calibration_value("abcone2threexyz")
        self.assertEqual(value, "abc123xyz")

    def test_parse_calibration_case_three(self):
        value = part2.parse_calibration_value("abc123xyz")
        self.assertEqual(value, 13)

    def test_correct_calibration_case_four(self):
        value = part2.correct_calibration_value("xtwone3four")
        self.assertEqual(value, "x2ne34")

    def test_parse_calibration_case_four(self):
        value = part2.parse_calibration_value("x2ne34")
        self.assertEqual(value, 24)

    def test_correct_calibration_case_five(self):
        value = part2.correct_calibration_value("4nineeightseven2")
        self.assertEqual(value, "49872")

    def test_parse_calibration_case_five(self):
        value = part2.parse_calibration_value("49872")
        self.assertEqual(value, 42)

    def test_correct_calibration_case_six(self):
        value = part2.correct_calibration_value("zoneight234")
        self.assertEqual(value, "z1ight234")

    def test_parse_calibration_case_six(self):
        value = part2.parse_calibration_value("z1ight234")
        self.assertEqual(value, 14)

    def test_correct_calibration_case_seven(self):
        value = part2.correct_calibration_value("7pqrstsixteen")
        self.assertEqual(value, "7pqrst16")

    def test_parse_calibration_case_seven(self):
        value = part2.parse_calibration_value("7pqrst16")
        self.assertEqual(value, 76)

    def test_find_sum(self):
        data = [29, 83, 13, 24, 42, 14, 76]
        self.assertEqual(part2.find_sum(data), 281)


if __name__ == "__main__":
    unittest.main()
