import re
from itertools import product


def read_data(filename):
    with open(filename, mode='r') as file:
        for line in file:
            parts = line.rstrip('\n').split()
            yield parts[0], [int(number) for number in parts[1].split(',')]


def find_number_of_possible_solutions(giant_filed_record, different_format_record):
    translation = [['#', '.'] if char == '?' else char for char in giant_filed_record]

    solution_count = 0

    for combination in product(*translation):
        matches = re.findall(pattern=r'#+', string=''.join(combination))
        if [len(match) for match in matches] == different_format_record:
            solution_count += 1

    return solution_count


if __name__ == '__main__':
    data_generator = read_data('../input/12.txt')
    # data_generator = read_data('../test_input/12.txt')  # 21

    result = 0

    while record_set := next(data_generator, None):
        result += find_number_of_possible_solutions(record_set[0], record_set[1])

    print(result)
