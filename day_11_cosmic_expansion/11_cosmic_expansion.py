from itertools import combinations


def read_data(filename):
    with open(filename, mode='r') as file:
        return [tuple([element for element in line.rstrip('\n')]) for line in file]


def expand_universe(universe):
    no_galaxies = [row_no for row_no, row in enumerate(universe) if '#' not in row]
    for row_no in no_galaxies[::-1]:
        universe.insert(row_no, tuple(['.'] * len(universe[0])))

    universe = list(zip(*universe))

    no_galaxies = [column_no for column_no, column in enumerate(universe) if '#' not in column]
    for column_no in no_galaxies[::-1]:
        universe.insert(column_no, tuple(['.'] * len(universe[0])))

    universe = list(zip(*universe))

    return universe


def find_galaxies(universe):
    return [(row_no, col_no) for row_no, row in enumerate(universe) for col_no, cell in enumerate(row) if cell == '#']


def calculate_distances_between_galaxies(galaxies):
    return sum([abs(y1 - y2) + (abs(x1 - x2)) for (y1, x1), (y2, x2) in combinations(galaxies, 2)])


if __name__ == '__main__':
    universe_data = read_data('../input/11.txt')
    # universe_data = read_data('../test_input/11.txt')  # 374

    expanded_universe = expand_universe(universe_data)
    all_galaxies = find_galaxies(expanded_universe)
    result = calculate_distances_between_galaxies(all_galaxies)
    print(result)
