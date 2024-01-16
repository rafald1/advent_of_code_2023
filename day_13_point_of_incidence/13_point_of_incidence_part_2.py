from itertools import chain


def read_data(filename):
    with open(filename, mode='r') as file:
        for section in file.read().split('\n\n'):
            yield [tuple(row) for row in section.split('\n')]


def check_for_reflection(pattern):
    no_of_rows = len(pattern)
    for row_no in range(1, no_of_rows):
        above = pattern[:row_no] if row_no < no_of_rows / 2 else pattern[2 * row_no - no_of_rows:row_no]
        under = pattern[row_no:2 * row_no][::-1]

        above = list(chain(*above))
        under = list(chain(*under))

        diff_count = sum([1 for index in range(len(above)) if above[index] != under[index]])
        if diff_count == 1:
            return row_no

    return 0


if __name__ == '__main__':
    data_generator = read_data('../input/13.txt')
    # data_generator = read_data('../test_input/13.txt')  # 400

    result = 0

    while fetched_pattern := next(data_generator, None):
        result += check_for_reflection(fetched_pattern) * 100
        result += check_for_reflection(list(zip(*fetched_pattern)))

    print(result)
