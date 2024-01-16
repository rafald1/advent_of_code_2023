def read_data(filename):
    with open(filename, mode='r') as file:
        return [line.rstrip('\n') for line in file]


def calculate_load_on_north_support_beams(platform):
    return sum([line.count('O') * (line_no + 1) for line_no, line in enumerate(platform[::-1])])


def move_rocks_spin_cycle(platform):
    # move rocks north: rotate platform by 90 degree counterclockwise, move rocks west, restore platform position
    platform = [''.join(list(line)) for line in zip(*platform)]
    platform = ['#'.join([''.join(sorted(section, reverse=True)) for section in line.split('#')]) for line in platform]
    platform = [''.join(list(line)) for line in zip(*platform)]

    # move rocks west
    platform = ['#'.join([''.join(sorted(section, reverse=True)) for section in line.split('#')]) for line in platform]

    # move rocks south: rotate platform by 90 degree counterclockwise, move rocks east, restore platform position
    platform = [''.join(list(line)) for line in zip(*platform)]
    platform = ['#'.join([''.join(sorted(section)) for section in line.split('#')]) for line in platform]
    platform = [''.join(list(line)) for line in zip(*platform)]

    # move rocks east
    platform = ['#'.join([''.join(sorted(section)) for section in line.split('#')]) for line in platform]

    return platform


def predict_platform_data(platform, cycle_no):
    platform_history = []

    counter = 0
    while platform not in platform_history:
        platform_history.append(platform)
        platform = move_rocks_spin_cycle(platform)
        counter += 1

    offset = platform_history.index(platform)
    cycle_length = counter - offset

    return platform_history[offset + (cycle_no - offset) % cycle_length] if cycle_no > offset else platform_history[cycle_no]


if __name__ == '__main__':
    platform_data = read_data('../input/14.txt')
    # platform_data = read_data('../test_input/14.txt')  # 64

    predicted_platform_data = predict_platform_data(platform_data, cycle_no=1_000_000_000)
    result = calculate_load_on_north_support_beams(predicted_platform_data)
    print(result)
