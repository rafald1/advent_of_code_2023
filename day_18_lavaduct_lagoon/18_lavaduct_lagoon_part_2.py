def read_data(filename):
    with open(filename, mode='r') as file:
        return [(int(line.rstrip()[-7:-2], 16), int(line.rstrip()[-2])) for line in file]


def dig_border(plan):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Right, Down, Left, Up
    border = [(0, 0)]
    border_length = 0

    for length, direction in plan:
        border_length += length
        dx, dy = directions[direction]
        x, y = border[-1]
        border += [(x + dx * length, y + dy * length)]

    return border, border_length


def calculate_border_area(border):
    # Shoelace formula used
    area = [border[i - 1][0] * border[i][1] - border[i - 1][1] * border[i][0] for i in range(1, len(border))]
    return abs(sum(area)) / 2


def calculate_number_of_blocks_enclosed_by_border(border, border_length):
    # Pick's theorem
    # A = i + (b / 2) - 1

    b = border_length
    a = calculate_border_area(border)
    i = a - (b / 2) + 1

    return int(i)


if __name__ == '__main__':
    dig_plan = read_data('../input/18.txt')
    # dig_plan = read_data('../test_input/18.txt')  # 952408144115

    dug_border, dug_border_length = dig_border(dig_plan)
    blocks_inside = calculate_number_of_blocks_enclosed_by_border(dug_border, dug_border_length)

    print(dug_border_length + blocks_inside)
