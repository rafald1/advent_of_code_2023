import random
import sympy


def read_data(filename):
    with open(filename, mode='r') as file:
        return [[tuple(map(int, (values.split(',')))) for values in line.split('@')] for line in file]


def gauss_elimination(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])

    for i in range(num_rows):
        # re-sequence if the pivot is zero
        if matrix[i][i] == 0:
            for k in range(i + 1, num_rows):
                if matrix[k][i] != 0:
                    # swap the current row with the non-zero row
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    break
            else:
                # no non-zero element found in the current column
                # matrix is singular, cannot perform Gaussian elimination
                return None

        # pivot for the current row
        pivot = matrix[i][i]

        # make the diagonal element 1
        for j in range(i, num_cols):
            matrix[i][j] /= pivot

        # make the other rows 0 in the current column
        for k in range(num_rows):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, num_cols):
                    matrix[k][j] -= factor * matrix[i][j]


def find_three_hailstones_with_linearly_independent_velocity_vectors(hailstones):
    matrix = None

    while not matrix:
        hailstone_a, hailstone_b, hailstone_c = random.sample(hailstones, 3)
        _, (vector_a) = hailstone_a
        _, (vector_b) = hailstone_b
        _, (vector_c) = hailstone_c

        matrix = [list(vector) for vector in zip(vector_a, vector_b, vector_c)]

        if matrix:
            gauss_elimination(matrix)

            for row in matrix:  # check if any row is all zeros, indicating linear dependence
                if all(element == 0 for element in row):
                    matrix = None

        if matrix:
            return hailstone_a, hailstone_b, hailstone_c


def solve(hailstones):
    solution = []

    while not solution:
        independent_hailstones = find_three_hailstones_with_linearly_independent_velocity_vectors(hailstones)
        hailstone_a, hailstone_b, hailstone_c = independent_hailstones
        (px_a, py_a, pz_a), (vx_a, vy_a, vz_a) = hailstone_a
        (px_b, py_b, pz_b), (vx_b, vy_b, vz_b) = hailstone_b
        (px_c, py_c, pz_c), (vx_c, vy_c, vz_c) = hailstone_c

        px, py, pz, vx, vy, vz = sympy.symbols("px, py, pz, vx, vy, vz")

        equations = [
            sympy.Eq((px_a - px) / (vx - vx_a), (py_a - py) / (vy - vy_a)),
            sympy.Eq((px_a - px) / (vx - vx_a), (pz_a - pz) / (vz - vz_a)),
            sympy.Eq((px_b - px) / (vx - vx_b), (py_b - py) / (vy - vy_b)),
            sympy.Eq((px_b - px) / (vx - vx_b), (pz_b - pz) / (vz - vz_b)),
            sympy.Eq((px_c - px) / (vx - vx_c), (py_c - py) / (vy - vy_c)),
            sympy.Eq((px_c - px) / (vx - vx_c), (pz_c - pz) / (vz - vz_c)),
        ]

        solution = sympy.solve(equations, px, py, pz, vx, vy, vz)

    px, py, pz, _, _, _ = solution[0]
    return sum([px, py, pz])

    # collision with three hailstones is required to get enough equations to find
    # starting position (px, py, pz) and velocity (vx, vy, vz) of the rock

    # transforming a set of nine equations (1-9) to a set of six equations (I - VI) by eliminating t_a, t_b and t_c
    # (1) px + vx * t_a = px_a + vx_a * t_a -> t_a = (px_a - px) / (vx - vx_a)
    # (2) py + vy * t_a = py_a + vy_a * t_a -> t_a = (py_a - py) / (vy - vy_a)
    # (3) pz + vz * t_a = pz_a + vz_a * t_a -> t_a = (pz_a - pz) / (vz - vz_a)
    # (I) (px_a - px) / (vx - vx_a) = (py_a - py) / (vy - vy_a)
    # (II) (px_a - px) / (vx - vx_a) = (pz_a - pz) / (vz - vz_a)

    # (4) px + vx * t_b = px_b + vx_b * t_b -> t_b = (px_b - px) / (vx - vx_b)
    # (5) py + vy * t_b = py_b + vy_b * t_b -> t_b = (py_b - py) / (vy - vy_b)
    # (6) pz + vz * t_b = pz_b + vz_b * t_b -> t_b = (pz_b - pz) / (vz - vz_b)
    # (III) (px_b - px) / (vx - vx_b) = (py_b - py) / (vy - vy_b)
    # (IV) (px_b - px) / (vx - vx_b) = (pz_b - pz) / (vz - vz_b)

    # (7) px + vx * t_c = px_c + vx_c * t_c -> t_c = (px_c - px) / (vx - vx_c)
    # (8) py + vy * t_c = py_c + vy_c * t_c -> t_c = (py_c - py) / (vy - vy_c)
    # (9) pz + vz * t_c = pz_c + vz_c * t_c -> t_c = (pz_c - pz) / (vz - vz_c)
    # (V) (px_c - px) / (vx - vx_c) = (py_c - py) / (vy - vy_c)
    # (VI) (px_c - px) / (vx - vx_c) = (pz_c - pz) / (vz - vz_c)


if __name__ == '__main__':
    hailstones_data = read_data('../input/24.txt')
    # hailstones_data = read_data('../test_input/24.txt')  # 47

    result = solve(hailstones_data)

    print(result)
