"""
After reaching edges in original garden.
Red are odd and yellow are even steps.

| ⬜⬜⬜🟥⬜⬜⬜
| ⬜⬜🟥🟨🟥⬜⬜
| ⬜🟥🟨🟥🟨🟥⬜
| 🟥🟨🟥🟨🟥🟨🟥
| ⬜🟥🟨🟥🟨🟥⬜
| ⬜⬜🟥🟨🟥⬜⬜
| ⬜⬜⬜🟥⬜⬜⬜
|

Rotate by 45 degrees for better visualization.

| 🟥　🟥　🟥　🟥
| 　🟨　🟨　🟨
| 🟥　🟥　🟥　🟥
| 　🟨　🟨　🟨
| 🟥　🟥　🟥　🟥
| 　🟨　🟨　🟨
| 🟥　🟥　🟥　🟥
|

After reaching edge in the next gardens.

| ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟥🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜⬜⬜🟨🟥🟨🟥🟨⬜⬜⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜⬜
| ⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜
| ⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜
| ⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜
| 🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨
| ⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜
| ⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜
| ⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜
| ⬜⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜⬜🟨🟥🟨🟥🟨🟥🟨⬜⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜⬜⬜🟨🟥🟨🟥🟨⬜⬜⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨🟥🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜
| ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜🟨⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜
|

Rotate by 45 degrees for better visualization. There are 9 (3 * 3) somewhat similar areas.

| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
|
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
|
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
| 　🟥　🟥　🟥　　🟥　🟥　🟥　🟥　　🟥　🟥　🟥
| 🟨　🟨　🟨　🟨　　🟨　🟨　🟨　　🟨　🟨　🟨　🟨
|

Predicting... after reaching edge in next gardens there will be 25 (5 * 5) areas.

Then 49 (7 * 7) areas, 81 (9 * 9), 121 (11 * 11), ...

There is quadratic relationship here.
"""

from collections import deque


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


def count_plots(grid, start, steps_available):
    width, height = max(grid)
    directions = {(0, -1), (1, 0), (0, 1), (-1, 0)}
    queue = deque([((0, 0), start, steps_available)])
    seen = {((0, 0), start)}
    plot_count = 0

    while queue:
        (garden_x, garden_y), (x, y), steps_remaining = queue.popleft()

        if steps_remaining % 2 == 0:
            plot_count += 1

        if steps_remaining > 0:
            steps_remaining -= 1

            for dx, dy in directions:
                next_x, next_y = (x + dx, y + dy)

                if next_y < 0:  # n
                    next_y = height
                elif next_x > width:  # e
                    next_x = 0
                elif next_y > height:  # s
                    next_y = 0
                elif next_x < 0:  # w
                    next_x = width

                next_garden = garden_x + dx, garden_y + dy
                next_plot = (next_x, next_y)

                if next_plot not in grid or (next_garden, next_plot) in seen:
                    continue

                queue.append((next_garden, next_plot, steps_remaining))
                seen.add((next_garden, next_plot))

    return plot_count


def quadratic_function(grid, start, steps_available):
    width, height = max(grid)
    assert width == height
    grid_size = width + 1
    first_grid_step_number_to_edge = grid_size // 2
    assert (steps_available - first_grid_step_number_to_edge) % grid_size == 0
    step_numbers = [first_grid_step_number_to_edge + grid_size * i for i in range(3)]
    plots_count = [count_plots(grid, start, step_number) for step_number in step_numbers]

    # Three equations are needed to find: a, b and c in quadratic function y = a * x ** 2 + b * x + c.
    # y will be number of plots that have been reached for different x, where x is number of steps taken, so
    # in 65 (65 + 131 * 0) steps we reached plots_count[0], in 196 (65 + 131 * 1) we reached plots_count[1],
    # in 327 (65 + 131 * 2) we reached plots_count[2] and in 26501365 (65 + 131 * 202300) we will reach y plots.
    # To simplify solving equations x will represent number of whole grids in each number of steps so:
    # 0, 1, 2 and after finding a, b and c: 202300.
    # (1) plots_count[0] = a * 0 ** 2 + b * 0 + c ->
    c = plots_count[0]
    # (2) plots_count[1] = a * 1 ** 2 + b * 1 + c -> b = plots_count[1] - a - c ->
    # b = plots_count[1] - a - plots_count[0] -> (*)
    # (3) plots_count[2] = a * 2 ** 2 + b * 2 + c -> 4 * a = plots_count[2] - 2 * b - c ->
    # 4 * a = plots_count[2] - 2 * (plots_count[1] - a - plots_count[0]) - plots_count[0] ->
    # 4 * a = plots_count[2] - 2 * plots_count[1] + 2 * a + 2 * plots_count[0] - plots_count[0] ->
    # 2 * a = plots_count[2] - 2 * plots_count[1] + plots_count[0] ->
    a = (plots_count[2] - 2 * plots_count[1] + plots_count[0]) / 2
    # (*) b = plots_count[1] - ((plots_count[2] - 2 * plots_count[1] + plots_count[0]) / 2) - plots_count[0] ->
    b = 2 * plots_count[1] - (plots_count[2] + 3 * plots_count[0]) / 2

    x = 202300
    y = a * x ** 2 + b * x + c

    return int(y)


if __name__ == '__main__':
    grid_data, start_cell = read_data('../test_input/21.txt')
    assert count_plots(grid_data, start_cell, 6) == 16
    assert count_plots(grid_data, start_cell, 10) == 50
    assert count_plots(grid_data, start_cell, 50) == 1594
    assert count_plots(grid_data, start_cell, 100) == 6536
    assert count_plots(grid_data, start_cell, 500) == 167004
    assert count_plots(grid_data, start_cell, 1000) == 668697  # in less than 3 seconds
    # assert count_plots(grid_data, start_cell, 5000) == 16733044  # in 1186 seconds

    grid_data, start_cell = read_data('../input/21.txt')
    result = quadratic_function(grid_data, start_cell, 26501365)
    print(result)
