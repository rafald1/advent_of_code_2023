import re


def read_data(filename):
    with open(filename, mode='r') as file:
        for section in file.read().split('\n\n'):
            yield section


def find_seeds_numbers(section):
    seeds_found = re.findall(pattern=r'\d+', string=section)
    return [int(seed) for seed in seeds_found]


def convert_numbers_from_source_into_destination_category(section, seeds_numbers):
    for index, source_number in enumerate(seeds_numbers):
        for destination_source_range in re.findall(pattern=r'(\d+) (\d+) (\d+)', string=section):
            destination, source, range_length = map(int, destination_source_range)
            if source_number in range(source, source + range_length):
                seeds_numbers[index] = source_number - source + destination
    return seeds_numbers


if __name__ == '__main__':
    data = read_data('../input/05.txt')
    # data = read_data('../test_input/05.txt')  # 35
    seeds = find_seeds_numbers(next(data))

    while almanac_section := next(data, None):
        seeds = convert_numbers_from_source_into_destination_category(almanac_section, seeds)

    print(min(seeds))
