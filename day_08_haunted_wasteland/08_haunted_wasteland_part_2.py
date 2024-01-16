import re
import math


def read_data(filename):
    with open(filename, mode='r') as file:
        directions, raw_maps = file.read().split('\n\n')
        maps = {
            node: (left_dest, right_dest)
            for node, left_dest, right_dest in re.findall(pattern=r'(\w+) = \((\w+), (\w+)\)', string=raw_maps)
        }
    return directions, maps


def get_direction(directions):
    while True:
        for direction in directions:
            yield 0 if direction == 'L' else 1  # 'L' converted to 0, 'R' converted to 1


def find_path(maps, directions, starting_nodes):
    direction_generator = get_direction(directions)
    step_counters = []

    for node in starting_nodes:
        step_counter = 0

        while node[-1] != 'Z':
            direction = next(direction_generator)
            node = maps[node][direction]
            step_counter += 1

        step_counters.append(step_counter)

    return math.lcm(*step_counters)


if __name__ == '__main__':
    all_directions, all_maps = read_data('../input/08.txt')
    # all_directions, all_maps = read_data('../test_input/08_2.txt')  # 6

    all_starting_nodes = [node for node in all_maps.keys() if node[-1] == 'A']
    no_of_steps = find_path(all_maps, all_directions, starting_nodes=all_starting_nodes)
    print(no_of_steps)
