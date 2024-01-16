import re


def find_minimum_number_cubes_power(input_string):
    max_red_value = max(int(match) for match in re.findall(pattern=r'(\d+) red', string=input_string))
    max_green_value = max(int(match) for match in re.findall(pattern=r'(\d+) green', string=input_string))
    max_blue_value = max(int(match) for match in re.findall(pattern=r'(\d+) blue', string=input_string))

    return int(max_red_value) * int(max_green_value) * int(max_blue_value)


def process_data(filename):
    with open(filename, mode='r') as file:
        return sum(find_minimum_number_cubes_power(line) for line in file)


if __name__ == '__main__':
    assert process_data('../test_input/02.txt') == 2286

    result = process_data('../input/02.txt')
    print(result)
