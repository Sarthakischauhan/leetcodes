# adding some notes and information about the breadth first search algorithm on graphs
# simple implementation below.
from collections import deque

class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BFSclass():
	def __init__(self):
		self.q = deque([])
	
	def add(self, node):
		self.q.appendLeft(node)


# This is the actual code
def BFS(graph, start):
    visited = set()  # Keep track of the nodes that we've visited
    queue = deque([start])  # Use a queue to implement the BFS
    while queue:
       	node = queue.popleft()  # Dequeue a node from front of queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node, end=' ')  # Visit the node (print its value in this case)
            queue.extend(graph[node])  # Enqueue all neighbours

def DFS(graph,start):
    visited=set()
    q = deque([start])
    while q:
        node = q.popleft()
        if node not in visited:
            visited.add(node)
            print(f"Current node {node}")
            for n in graph[node][::-1]:
                if n not in visited:
                    q.appendleft(n)

# Use the BFS function on a graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}

BFS(graph, 'A')  # Output: A B C D E F
print("DFS starts here")
DFS(graph, "A")
