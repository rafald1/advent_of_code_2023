import re


def find_calibration_value(string):
    def get_digit(x):
        return x if x.isnumeric() else letter_digits.index(x) + 1

    letter_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    pattern = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'
    digits = re.findall(pattern, string)

    return int(f'{get_digit(digits[0])}{get_digit(digits[-1])}')


def process_data(filename):
    with open(filename, mode='r') as file:
        return sum(find_calibration_value(line) for line in file)


if __name__ == '__main__':
    assert process_data('../test_input/01_2.txt') == 281

    result = process_data('../input/01.txt')
    print(result)
