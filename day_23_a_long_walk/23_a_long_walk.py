def read_data(filename):
    with open(filename, mode='r') as file:
        return {(x, y): cell for y, line in enumerate(file) for x, cell in enumerate(line.rstrip())}


def build_graph(maze):
    directions = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}
    graph = {}
    start = (-1, -1)
    end = (-1, -1)

    for (x, y), cell in maze.items():
        if cell in '.^>v<':
            if y < start[1] or start[1] == -1:
                start = (x, y)
            if y > end[1]:
                end = (x, y)

            graph[(x, y)] = []

            for direction, (dx, dy) in directions.items():
                neighbour = x + dx, y + dy
                if neighbour in maze and (maze[neighbour] == '.' or maze[neighbour] == direction):
                    if maze[(x, y)] == '.' or maze[(x, y)] == direction:
                        graph[(x, y)].append(neighbour)

    return graph, start, end


def find_longest_path(graph, start, end):
    queue = [(start, set())]
    paths_found = []

    while queue:
        current_cell, visited = queue.pop()

        if current_cell == end:
            paths_found.append(len(visited))

        for neighbour in graph[current_cell]:
            if neighbour not in visited:
                queue.append((neighbour, visited | {current_cell}))

    return max(paths_found)


if __name__ == '__main__':
    maze_data = read_data('../input/23.txt')
    # maze_data = read_data('../test_input/23.txt')  # 94

    maze_graph, start_cell, end_cell = build_graph(maze_data)
    result = find_longest_path(maze_graph, start_cell, end_cell)
    print(result)
