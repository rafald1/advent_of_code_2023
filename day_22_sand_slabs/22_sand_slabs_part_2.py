from collections import defaultdict


def read_data(filename):
    with open(filename, mode='r') as file:
        return [[tuple(map(int, (x_y_z.split(',')))) for x_y_z in line.rstrip().split('~')] for line in file]


def sort_bricks(bricks):
    return sorted(bricks, key=lambda brick: min(z for _, _, z in brick))


def build_brick_stack(bricks):
    brick_stack = []
    z_level = defaultdict(int)  # storing highest z for every possible (x, y)
    falling_bricks_counter = 0

    for brick_no, brick in enumerate(bricks):
        (x1, y1, z1), (x2, y2, z2) = brick
        current_max_z = max([z_level[(x, y)] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)])
        new_z1 = current_max_z + 1
        new_z2 = current_max_z + 1 + z2 - z1
        brick_stack.append([(x1, y1, new_z1), (x2, y2, new_z2)])

        if z1 != new_z1:
            falling_bricks_counter += 1

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                z_level[(x, y)] = new_z2

    return brick_stack, falling_bricks_counter


def disintegrate(bricks):
    falling_bricks_counter = 0

    for index in range(len(bricks)):
        _, counter = build_brick_stack(bricks[:index] + bricks[index + 1:])
        falling_bricks_counter += counter

    return falling_bricks_counter


if __name__ == '__main__':
    sand_slabs = read_data('../input/22.txt')
    # sand_slabs = read_data('../test_input/22.txt')

    sorted_bricks = sort_bricks(sand_slabs)
    stacked_bricks, _ = build_brick_stack(sorted_bricks)

    result = disintegrate(stacked_bricks)
    print(result)
