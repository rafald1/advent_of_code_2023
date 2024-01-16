import re


def read_data(filename):
    with open(filename, mode='r') as file:
        for section in file.read().split('\n\n'):
            yield section


def find_seeds_start_and_end_numbers(section):
    seeds_and_ranges_found = re.findall(pattern=r'(\d+) (\d+)', string=section)
    return [(int(seed), int(seed) + int(range_length) - 1) for seed, range_length in seeds_and_ranges_found]


def build_section_map(section):
    return [
        tuple(map(int, destination_source_range))
        for destination_source_range in re.findall(pattern=r'(\d+) (\d+) (\d+)', string=section)
    ]


def convert_numbers_from_source_into_destination_category(seeds_map, section_map):
    new_seeds_map = []

    while seeds_map:
        seeds_start, seeds_end = seeds_map.pop(0)
        seed_range_found = False

        for destination_start, source_start, range_length in section_map:
            source_end = source_start + range_length - 1
            # a seeds range doesn't overlap a source range
            if seeds_end < source_start or seeds_start > source_end:
                continue  # check next source range
            # a seeds range fits into one source range
            elif seeds_start >= source_start and seeds_end <= source_end:
                new_seeds_map.append((destination_start + seeds_start - source_start,
                                      destination_start + range_length - 1 + seeds_end - source_end))
                seed_range_found = True
            # a seeds range starts before a source range
            elif seeds_start < source_start and seeds_end <= source_end:
                new_seeds_map.append((destination_start, destination_start + range_length - 1 + seeds_end - source_end))
                seeds_map.append((seeds_start, source_start - 1))
                seed_range_found = True
            # a seeds range ends after a source range
            elif seeds_start >= source_start and seeds_end > source_end:
                new_seeds_map.append((destination_start + seeds_start - source_start,
                                      destination_start + range_length - 1))
                seeds_map.append((source_end + 1, seeds_end))
                seed_range_found = True
            # a seeds range starts before and ends after a source range
            elif seeds_start < source_start and seeds_end > source_end:
                new_seeds_map.append((destination_start, destination_start + range_length - 1))
                seeds_map.append((seeds_start, source_start - 1))
                seeds_map.append((source_end + 1, seeds_end))
                seed_range_found = True
            break  # there is no need to check other source ranges, because you found one that matched

        if not seed_range_found:  # checked all source ranges and there was no match, so numbers stay unchanged
            new_seeds_map.append((seeds_start, seeds_end))

    return new_seeds_map


if __name__ == '__main__':
    data = read_data('../input/05.txt')
    # data = read_data('../test_input/05.txt')  # 46
    seed_ranges = find_seeds_start_and_end_numbers(next(data))

    while almanac_section := next(data, None):
        almanac_section_map = build_section_map(almanac_section)
        seed_ranges = convert_numbers_from_source_into_destination_category(seed_ranges, almanac_section_map)

    print(min(seed_ranges)[0])
