def read_data(filename):
    with open(filename, mode='r') as file:
        return [(direction, int(length)) for line in file for direction, length, _ in [line.strip().split()]]


def dig_border(plan):
    directions = {'U': (0, -1), 'R': (1, 0), 'D': (0, 1), 'L': (-1, 0)}
    border = [(0, 0)]
    for direction, length in plan:
        dx, dy = directions[direction]
        x, y = border[-1]
        border += [(x + dx * i, y + dy * i) for i in range(1, length + 1)]

    return border  # first and last element are the same, so border length is one less


def calculate_border_area(border):
    # Shoelace formula used
    area = [border[i - 1][0] * border[i][1] - border[i - 1][1] * border[i][0] for i in range(1, len(border))]
    return abs(sum(area)) / 2


def calculate_number_of_blocks_enclosed_by_border(border):
    # Pick's theorem
    # A = i + (b / 2) - 1

    b = len(border) - 1
    a = calculate_border_area(border)
    i = a - (b / 2) + 1

    return int(i)


if __name__ == '__main__':
    dig_plan = read_data('../input/18.txt')
    # dig_plan = read_data('../test_input/18.txt')  # 62

    dug_border = dig_border(dig_plan)
    blocks_inside = calculate_number_of_blocks_enclosed_by_border(dug_border)

    border_cells = len(dug_border) - 1

    print(border_cells + blocks_inside)
