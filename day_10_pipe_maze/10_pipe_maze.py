def read_data(filename):
    with open(filename, mode='r') as file:
        return [line.rstrip('\n') for line in file]


def build_neighbours_map_and_find_starting_cell(maze):
    start_row_no, start_column_no = -1, -1
    neighbours_map = {}
    for row_no, row in enumerate(maze):
        for column_no, cell in enumerate(row):
            neighbours_map[row_no, column_no] = []
            if cell in '|JL':  # add top neighbour
                neighbours_map[row_no, column_no].append((row_no - 1, column_no))
            if cell in '|7F':  # add bottom neighbour
                neighbours_map[row_no, column_no].append((row_no + 1, column_no))
            if cell in '-7J':  # add left neighbour
                neighbours_map[row_no, column_no].append((row_no, column_no - 1))
            if cell in '-FL':  # add right neighbour
                neighbours_map[row_no, column_no].append((row_no, column_no + 1))
            if cell == 'S':
                start_row_no, start_column_no = row_no, column_no

    # find neighbours of starting cell
    for key, value in neighbours_map.items():
        if (start_row_no, start_column_no) in value:
            neighbours_map[start_row_no, start_column_no].append(key)

    return neighbours_map, (start_row_no, start_column_no)


def calculate_farthest_point_from_start(maze):
    neighbours_map, starting_cell = build_neighbours_map_and_find_starting_cell(maze)
    next_cells = [starting_cell]
    visited_cells = [starting_cell]

    while next_cells:
        next_cell = next_cells.pop(0)
        for neighbour_cell in neighbours_map[next_cell]:
            if neighbour_cell not in visited_cells:
                visited_cells.append(neighbour_cell)
                next_cells.append(neighbour_cell)

    return int(len(visited_cells) / 2)


if __name__ == "__main__":
    data = read_data('../input/10.txt')
    # data = read_data('../test_input/10_1_1.txt')  # 4
    # data = read_data('../test_input/10_1_2.txt')  # 8

    result = calculate_farthest_point_from_start(data)
    print(result)
