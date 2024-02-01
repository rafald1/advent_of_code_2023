def read_data(filename):
    with open(filename, mode='r') as file:
        return [line.rstrip() for line in file]


def determine_new_direction(cell, direction):
    match cell:
        case '/':
            match direction:
                case '^':
                    return '>'
                case '>':
                    return '^'
                case 'v':
                    return '<'
                case '<':
                    return 'v'
        case '\\':
            match direction:
                case '^':
                    return '<'
                case '>':
                    return 'v'
                case 'v':
                    return '>'
                case '<':
                    return '^'
        case '-' if direction in '^v':
            return '><'
        case '|' if direction in '><':
            return '^v'

    return direction


def energize(grid, start_cell):
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    queue = [start_cell]
    energized_cells = set()

    while queue:
        (y, x), direction = queue.pop()

        if y == -1 or x == -1 or y == len(grid) or x == len(grid[0]) or ((y, x), direction) in energized_cells:
            continue  # skip when cell is out of bounds or when beam already traveled through to prevent going in loops

        energized_cells.add(((y, x), direction))

        new_directions = determine_new_direction(grid[y][x], direction)
        for new_direction in new_directions:
            dy, dx = directions[new_direction]
            queue.append([(y + dy, x + dx), new_direction])

    return len(set([cell for cell, _ in energized_cells]))


def find_all_starting_cells(grid):
    grid_width, grid_height = len(grid[0]), len(grid)
    all_starting_cells = []

    for i in range(grid_width):
        all_starting_cells.append([(0, i), 'v'])
        all_starting_cells.append([(grid_height - 1, i), '^'])

    for i in range(grid_height):
        all_starting_cells.append([(i, 0), '>'])
        all_starting_cells.append([(i, grid_width - 1), '<'])

    return all_starting_cells


if __name__ == '__main__':
    layout = read_data('../input/16.txt')
    # layout = read_data('../test_input/16.txt')  # 51

    starting_cells = find_all_starting_cells(layout)
    energized = []
    for starting_cell in starting_cells:
        energized += [energize(layout, starting_cell)]
    print(max(energized))
