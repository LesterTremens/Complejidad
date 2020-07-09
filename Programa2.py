parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
	else:
	    parent[root1] = root2
	if rank[root1] == rank[root2]: rank[root2] += 1

def tsp(graph):
    for vertice in graph['vertices']:
	make_set(vertice)
	minimum_spanning_tree = set()
	edges = list(graph['edges'])
	edges.sort()
	#print edges
    for edge in edges:
	weight, vertice1, vertice2 = edge
	if find(vertice1) != find(vertice2):
	    union(vertice1, vertice2)
	    minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)

graph = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'edges': set([
(7, 'A', 'B'),
(3, 'A', 'C'),
(8, 'A', 'D'),
(6, 'A', 'E'),
(1, 'A', 'F'),
(4, 'A', 'G'),
(7, 'B', 'A'),
(8, 'B', 'C'),
(9, 'B', 'D'),
(7, 'B', 'E'),
(1, 'B', 'F'),
(5, 'B', 'G'),
(8, 'C', 'A'),
(5, 'C', 'B'),
(8, 'C', 'D'),
(5, 'C', 'E'),
(4, 'C', 'F'),
(3, 'C', 'G'),
(5, 'D', 'A'),
(9, 'D', 'B'),
(1, 'D', 'C'),
(7, 'D', 'E'),
(5, 'D', 'F'),
(2, 'D', 'G'),
(7, 'E', 'A'),
(2, 'E', 'B'),
(1, 'E', 'C'),
(3, 'E', 'D'),
(9, 'E', 'F'),
(7, 'E', 'G'),
(6, 'F', 'A'),
(2, 'F', 'B'),
(5, 'F', 'C'),
(7, 'F', 'D'),
(8, 'F', 'E'),
(11, 'F', 'G'),
(9, 'G', 'A'),
(7, 'G', 'B'),
(6, 'G', 'C'),
(4, 'G', 'D'),
(2, 'G', 'E'),
(8, 'G', 'F'),
])
}

print tsp(graph)
