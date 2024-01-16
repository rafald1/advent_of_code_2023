import re


def read_data(filename):
    with open(filename, mode='r') as file:
        directions, raw_maps = file.read().split('\n\n')
        maps = {
            node: (left_dest, right_dest)
            for node, left_dest, right_dest in re.findall(pattern=r'([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)', string=raw_maps)
        }
    return directions, maps


def get_direction(directions):
    while True:
        for direction in directions:
            yield 0 if direction == 'L' else 1


def find_path(maps, directions, starting_node, ending_node):
    direction_generator = get_direction(directions)
    node = starting_node
    step_counter = 0

    while node != ending_node:
        direction = next(direction_generator)
        node = maps[node][direction]
        step_counter += 1

    return step_counter


if __name__ == '__main__':
    all_directions, all_maps = read_data('../test_input/08_1_1.txt')
    assert find_path(all_maps, all_directions, starting_node='AAA', ending_node='ZZZ') == 2
    all_directions, all_maps = read_data('../test_input/08_1_2.txt')
    assert find_path(all_maps, all_directions, starting_node='AAA', ending_node='ZZZ') == 6

    all_directions, all_maps = read_data('../input/08.txt')
    no_of_steps = find_path(all_maps, all_directions, starting_node='AAA', ending_node='ZZZ')
    print(no_of_steps)
