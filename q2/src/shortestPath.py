# Python program to find single source shortest paths 
# in a Directed Acyclic Graph (DAG). 
from collections import defaultdict
# V represents the number of Vertices, present 
# in the given DAG.
V=6
# INF means infinity, which is taken
# as a very large number.
INF=999999999999
# Node class
class Node:
    # v is the vertex, 
    # and wt is the weight.
    def __init__(self, _v, _wt):
        self.v=_v
        self.wt=_wt

# Graph Class
class Graph:
    def __init__(self,V):
        # Initializing Adajency list.
        self.adj=defaultdict(list)
        self.V=V
    # Function to add edge u->v of weigth wt.
    def addEdge(self, u, v, wt):
        self.adj[u].append(Node(v,wt))
        

    # Function to find topological Sort which is always possible
    # as the given graph is a DAG.
    def topologicalSort(self, v, visited, st):
        # Marking v as visited.
        
        visited[v]=True
        # Iterating for all the adjacent nodes of v.
        for node in self.adj[v]:
            
            # If any adjacent node to v is not 
            # visited, call topologicalSort function on it.
            if(visited[node.v]==False):
                self.topologicalSort(node.v, visited, st)
            
        
        # Push v into Stack
        st.append(v)
    

    # Function to compute the shortest path 
    # to all other vertices starting from src.
    def shortestPath(self, src):
        
        # Declare a Stack (st) which is used to find 
        # the topological sort of the given DAG.
        st=[]

        # Declare a dist array where dist[i] denotes
        # shortest distance of src from i. 
        # Initialize all it's entries with INF and 
        # dist[src] with 0.
        dist=[INF]*self.V
        # for(i in range(V)):
        #     dist[i]=INF

        # Create boolean visited array to keep track 
        # of visited elements.
        visited = [False]*self.V
        # for(int i=0i<Vi++)
        #     visited[i]=false
        # Iterate for all the V vertices.
        for i in range(V):
            # If 'i' found to unvisited call 
            # topoplogicalSort from there.
            if visited[i] == False:
                self.topologicalSort(i,visited,st)
        src = st[-1]
        dist[src] = 0
        print(st)     
        
        # Iterate till the stack is not empty.
        while len(st)>0:
            # Pop element from stack and store it in u.
            u=st.pop()

            # If shortest distance from src to u is 
            # not infinity i.e. it is reachable.
            
            if dist[u]!=INF:
                # Iterate for all the adjacent vertices 
                # of u.
                for node in self.adj[u]:
                    # If distance of src->v is greater than
                    # distance of src->u + u->v then update
                    # the value as shown.
                    if dist[node.v] > dist[u]+node.wt:
                        dist[node.v] = dist[u] + node.wt
        
        # Prinit the distances.
        for i in range(V):
            if dist[i]==INF:
                print("INF"),
            else:
                print(dist[i]),
        

import re
import sys

filename = sys.argv[1]

f = open(filename, "r")
lines = f.read().split("\n")[:-1]
f.close()

edges = [list(map(int,re.findall(r"\d+", line))) for line in lines]

g=Graph(V)
# Add edges.
for u,v in edges:
    g.addEdge(u,v,1)

# Find the shortest path from a 
# vertex (here 0).
g.shortestPath(1)
