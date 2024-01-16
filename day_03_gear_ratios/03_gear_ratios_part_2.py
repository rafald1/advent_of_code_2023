import re
import operator


def read_data(filename):
    with open(filename, mode='r') as file:
        return [line.rstrip('\n') for line in file]


def find_gear_ratios(engine_schematic):
    gears = {}
    for row_index, row in enumerate(engine_schematic):
        # locate all gears (*) and store their positions (row number and column number)
        for match in re.finditer(pattern=r'\*', string=row):
            gears[(row_index, match.start())] = []

    for row_index, row in enumerate(engine_schematic):
        for match in re.finditer(pattern=r'\d+', string=row):
            # for every number found check if indices of cells around are present in gears dictionary
            for row_no in [row_index - 1, row_index, row_index + 1]:
                for column_no in range(match.start() - 1, match.end() + 1):
                    if (row_no, column_no) in gears:
                        # store the number
                        gears[(row_no, column_no)].append(int(match.group()))

    return sum([operator.mul(*numbers) for numbers in gears.values() if len(numbers) >= 2])


if __name__ == '__main__':
    test_data = read_data('../test_input/03.txt')
    assert find_gear_ratios(test_data) == 467835

    data = read_data('../input/03.txt')
    result = find_gear_ratios(data)
    print(result)
