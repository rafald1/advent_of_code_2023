from itertools import combinations


def read_data(filename):
    with open(filename, mode='r') as file:
        return [tuple([element for element in line.rstrip('\n')]) for line in file]


def find_sections_without_galaxies(universe):
    rows_without_galaxies = [row_no for row_no, row in enumerate(universe) if '#' not in row]
    rotated_universe = list(zip(*universe))
    columns_without_galaxies = [column_no for column_no, column in enumerate(rotated_universe) if '#' not in column]

    return rows_without_galaxies, columns_without_galaxies


def find_galaxies(universe):
    return [(row_no, col_no) for row_no, row in enumerate(universe) for col_no, cell in enumerate(row) if cell == '#']


def calculate_distances_between_galaxies(galaxies, rows_and_columns_without_galaxies, expansion_rate):
    rows_without_galaxies, columns_without_galaxies = rows_and_columns_without_galaxies
    distances = []

    for (y1, x1), (y2, x2) in combinations(galaxies, 2):
        y1, y2 = sorted((y1, y2))
        distance_y = y2 - y1 + sum(expansion_rate - 1 for row_no in rows_without_galaxies if row_no in range(y1, y2))

        x1, x2 = sorted((x1, x2))
        distance_x = x2 - x1 + sum(expansion_rate - 1 for col_no in columns_without_galaxies if col_no in range(x1, x2))

        distances.append(distance_y + distance_x)

    return sum(distances)


if __name__ == '__main__':
    universe_data = read_data('../test_input/11.txt')  #
    all_galaxies = find_galaxies(universe_data)
    sections_without_galaxies = find_sections_without_galaxies(universe_data)
    assert calculate_distances_between_galaxies(all_galaxies, sections_without_galaxies, expansion_rate=10) == 1030
    assert calculate_distances_between_galaxies(all_galaxies, sections_without_galaxies, expansion_rate=100) == 8410

    universe_data = read_data('../input/11.txt')
    all_galaxies = find_galaxies(universe_data)
    sections_without_galaxies = find_sections_without_galaxies(universe_data)
    result = calculate_distances_between_galaxies(all_galaxies, sections_without_galaxies, expansion_rate=1_000_000)
    print(result)
