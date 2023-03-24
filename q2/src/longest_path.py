import re
import sys

# read in the input file
filename = sys.argv[1]

graph = {}
with open(filename) as f:
    for line in f:
        u,v = list(map(int, re.findall(r"\d+", line)))
        graph[u] = graph.get(u, []) + [v]

def sources(graph: dict[int, list[int]]) -> list[int]:
    """return a list of nodes with an indegree of 0 in the graph passed"""
    indegrees = {i: 0 for i in graph.keys()}
    for u in graph.keys():
        for v in graph[u]:
            indegrees[v] = indegrees.get(v, 0) + 1
    return [v for v, indegree in indegrees.items() if indegree == 0] 

def toposort(graph: dict[int, list[int]]) -> list[int]:
    """return an ordering of nodes in the graph such that if there is
       an edges from (u,v) u precedes v in the ordering"""
    # stores our topological ordering
    stack = []
    # stack to keep track of nodes with indegree 0
    zeroes = []
    # hold indegrees for each node
    indegrees = {i: 0 for i in graph.keys()}

    # calculate indegrees for each node
    for u in list(graph.keys()):
        for v in graph[u]:
            graph[v] = graph.get(v, [])
    for u in graph.keys():
        for v in graph[u]:
            indegrees[v] = indegrees.get(v, 0) + 1

    # append nodes of indegree 0 to stack of zeroes
    for i,degree in indegrees.items():
        if degree == 0:
            zeroes.append(i)

    # as long as there are still nodes left of indegree 0:
    while zeroes:
        u = zeroes.pop()
        stack.append(u)

        for v in graph[u]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                zeroes.append(v)
    
    return stack

def longestpath(graph: dict[int, list[int]], src: int) -> (dict[int, int], dict[int, int]):
    """return a tuple of a dictionary of containing distances from src to 
       every other node, along with a prev dictionary mapping each node v to 
       it's previous node u in the shortest path from src -> u
       prev[v] = v if v is the start of a path"""
    order = toposort(graph)

    INF = float("Inf")
    distances = {i: INF for i in graph.keys()}
    distances[src] = 0
    prev = {i: i for i in graph.keys()}

    for u in order:
        for v in graph[u]:
            if distances[u] - 1 < distances[v]:
                distances[v] = distances[u] - 1
                prev[v] = u

    return (distances, prev)

# calculate shortest paths for all sources in the graph:
#   the absolute shortest path in the graph must be one of these
longest_prev = []
longest_dist = -10**9
longest_dest = 0
for s in sources(graph): 
    (lengths, prev) = longestpath(graph, s)
    INF = float("Inf")

    nopaths = [i for i,dist in lengths.items() if dist == INF]
    lengths = {i: abs(dist) for i,dist in lengths.items() if dist != INF}
    
    furthest_node = max(lengths, key=lengths.get)

    if lengths[furthest_node] > longest_dist:
        longest_dist = lengths[furthest_node]
        longest_prev = prev
        longest_dest = furthest_node

# recover the longest path from the prev array
node = longest_dest
path = [0 for i in range(longest_dist+1)]

for i in reversed(range(longest_dist+1)):
    path[i] = node
    node = longest_prev[node]

print(f"The longest path in the graph is {path} of length {longest_dist}")

