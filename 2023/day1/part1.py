#!/bin/python
#
# What is the sum of all of the calibration values?

import re


def parse_calibration_value(data):
    # match the first and last number in each string
    first_num_re = re.compile(r"(\d)")
    last_num_re = re.compile(r"(\d)(?!.*\d)")

    first_num = first_num_re.search(data).group(0)
    last_num = last_num_re.search(data).group(0)

    return int(first_num + last_num)


def find_sum(data):
    sum = 0

    for line in data:
        sum = sum + int(line)

    return sum


if __name__ == "__main__":
    data = []
    with open("input1", "r") as input:
        for line in input:
            data.append(line)

    # Parse lines
    calibration_values = []
    for line in data:
        calibration_values.append(parse_calibration_value(line))
    # Sum Lines
    print(find_sum(calibration_values))
