def find_paths(graph, start, end, way=None):
    if way is None:
        way = []
    way = way + [start]
    if start == end:
        return [way]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in way:
            new_paths = find_paths(graph, node, end, way)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


graph_example = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': [], 'E': ['F'], 'F': []}
begin = 'A'
final = 'F'
ways = find_paths(graph_example, begin, final)
for path in ways:
    print(path)
