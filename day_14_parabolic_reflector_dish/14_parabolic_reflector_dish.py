def read_data(filename):
    with open(filename, mode='r') as file:
        return [line.rstrip('\n') for line in file]


def calculate_load_on_north_support_beams(platform):
    return sum([line.count('O') * (line_no + 1) for line_no, line in enumerate(platform[::-1])])


def move_rocks_north(platform):
    platform = [''.join(list(line)) for line in zip(*platform)]
    platform = ['#'.join([''.join(sorted(section, reverse=True)) for section in line.split('#')]) for line in platform]
    platform = [''.join(list(line)) for line in zip(*platform)]
    return platform


if __name__ == '__main__':
    platform_data = read_data('../input/14.txt')
    # platform_data = read_data('../test_input/14.txt')  # 136

    platform_data = move_rocks_north(platform_data)
    result = calculate_load_on_north_support_beams(platform_data)
    print(result)
