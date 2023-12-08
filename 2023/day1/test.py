import unittest
import part1


class TestPartOne(unittest.TestCase):
    def setUp(self):
        self.data = []

    def test_case_one(self):
        value = part1.parse_calibration_value("1abc2")
        self.data.append(value)
        self.assertEqual(value, 12)

    def test_case_two(self):
        value = part1.parse_calibration_value("pqr3stu8vwx")
        self.data.append(value)
        self.assertEqual(value, 38)

    def test_case_three(self):
        value = part1.parse_calibration_value("a1b2c3d4e5f")
        self.data.append(value)
        self.assertEqual(value, 15)

    def test_case_four(self):
        value = part1.parse_calibration_value("treb7uchet")
        self.data.append(value)
        self.assertEqual(value, 77)

    def test_final_answer(self):
        self.assertEqual(part1.find_sum(self.data), 142)


if __name__ == "__main__":
    unittest.main()
