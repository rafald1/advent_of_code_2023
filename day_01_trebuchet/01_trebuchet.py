def find_calibration_value(string):
    first_num = next((char for char in string if char.isnumeric()), None)
    last_num = next((char for char in reversed(string) if char.isnumeric()), None)

    if first_num is not None and last_num is not None:
        return int(f'{first_num}{last_num}')
    else:
        return 0


def process_data(filename):
    with open(filename, mode='r') as file:
        return sum(find_calibration_value(line) for line in file)


if __name__ == '__main__':
    assert process_data('../test_input/01_1.txt') == 142

    result = process_data('../input/01.txt')
    print(result)

