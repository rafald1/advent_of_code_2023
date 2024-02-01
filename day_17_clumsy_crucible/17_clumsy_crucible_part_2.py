from heapq import heappush, heappop


def read_data(filename):
    with open(filename, mode='r') as file:
        return [[int(num) for num in line.rstrip()] for line in file]


def determine_new_directions(direction):
    match direction:
        case '^' | 'v':
            return '><'
        case '>' | '<':
            return '^v'


def find_path(grid):
    grid_width, grid_height = len(grid[0]), len(grid)
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

    start_cell = (0, 0)
    y, x = start_cell
    end_cell = (grid_height - 1, grid_width - 1)

    queue = [(0, (y, x), ('>', 0)), (0, (y, x), ('v', 0))]
    visited = set()

    while queue:
        heat_loss, (y, x), (direction, direction_count) = heappop(queue)

        if (y, x) == end_cell:
            return heat_loss

        if ((y, x), (direction, direction_count)) in visited:
            continue

        visited.add(((y, x), (direction, direction_count)))

        if direction_count < 10:
            dy, dx = directions[direction]
            next_y, next_x = y + dy, x + dx
            if -1 < next_y < grid_height and -1 < next_x < grid_width:
                heappush(queue, (heat_loss + grid[next_y][next_x], (next_y, next_x), (direction, direction_count + 1)))

        if direction_count >= 4:
            new_directions = determine_new_directions(direction)
            for direction in new_directions:
                dy, dx = directions[direction]
                next_y, next_x = y + dy, x + dx

                if -1 < next_y < grid_height and -1 < next_x < grid_width:
                    heappush(queue, (heat_loss + grid[next_y][next_x], (next_y, next_x), (direction, 1)))


if __name__ == '__main__':
    puzzle_map = read_data('../input/17.txt')
    # puzzle_map = read_data('../test_input/17.txt')  # 94

    result = find_path(puzzle_map)
    print(result)
