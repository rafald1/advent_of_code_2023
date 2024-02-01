from collections import defaultdict


def read_data(filename):
    with open(filename, mode='r') as file:
        return {(x, y): cell for y, line in enumerate(file) for x, cell in enumerate(line.rstrip())}


def build_graph(maze):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # ^>v<
    graph = defaultdict(list)

    for (x, y), cell in maze.items():
        if cell != '#':
            for (dx, dy) in directions:
                neighbour = x + dx, y + dy
                if neighbour in maze and maze[neighbour] != '#':
                    graph[(x, y)].append(neighbour)

    return graph


def find_vertices_start_end(graph):
    start_end = set()
    nodes = set()

    for (x, y), neighbours in graph.items():
        no_of_neighbours = len(neighbours)
        if no_of_neighbours == 1:
            start_end.add((x, y))
        if no_of_neighbours != 2:
            nodes.add((x, y))

    return nodes, start_end


def find_edges(graph, nodes):
    edges = defaultdict(list)

    for node in nodes:
        queue = [(node, set())]

        while queue:
            (x, y), visited = queue.pop()

            for neighbour in graph[(x, y)]:
                if neighbour not in visited:
                    if neighbour in nodes:
                        edges[node].append((neighbour, len(visited) + 1))
                    else:
                        queue.append((neighbour, visited | {(x, y)}))

    return edges


def find_longest_path(edges, start, end):
    path_distances = []
    queue = [(start, set(), 0)]

    while queue:
        (x, y), visited, distance = queue.pop()

        if (x, y) == end:
            path_distances.append(distance)
            continue

        for neighbour_node, weight in edges[(x, y)]:
            if neighbour_node not in visited:
                queue.append((neighbour_node, visited | {(x, y)}, distance + weight))

    return max(path_distances)


if __name__ == '__main__':
    maze_data = read_data('../input/23.txt')
    # maze_data = read_data('../test_input/23.txt')  # 154

    maze_graph = build_graph(maze_data)
    all_nodes, (start_node, end_node) = find_vertices_start_end(maze_graph)
    all_edges = find_edges(maze_graph, all_nodes)
    result = find_longest_path(all_edges, start_node, end_node)
    print(result)
