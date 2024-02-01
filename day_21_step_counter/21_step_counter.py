def read_data(filename):
    with open(filename, mode='r') as file:
        grid = set()

        for y, line in enumerate(file):
            for x, cell in enumerate(line.rstrip()):
                if cell != '#':
                    grid.add((x, y))
                if cell == 'S':
                    start = (x, y)

    return grid, start


def count_plots(grid, start, possible_steps):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    odd_plots = set()
    even_plots = {start}
    all_plots = [odd_plots, even_plots]

    for step in range(1, possible_steps + 1):
        odd_or_even = step % 2
        for x, y in all_plots[odd_or_even]:
            for dx, dy in directions:
                next_cell = x + dx, y + dy
                if next_cell in grid and next_cell not in all_plots[odd_or_even - 1]:
                    all_plots[odd_or_even - 1].add(next_cell)

    return len(odd_plots) if possible_steps % 2 == 1 else len(even_plots)


if __name__ == '__main__':
    garden_grid, starting_cell = read_data('../input/21.txt')
    result = count_plots(garden_grid, starting_cell, 64)

    # garden_grid, starting_cell = read_data('../test_input/21.txt')  # 16
    # result = count_plots(garden_grid, starting_cell, 6)

    print(result)
