class Solution:
def minReorder(self, n: int, connections: List[List[int]]) -> int:
    edges = {(a, b) for a, b in connections}  
    neighbors = {i: [] for i in range(n)}    
    visited = set()
    count = 0
    
    for city, neighbor in connections:
        neighbors[city].append(neighbor)
        neighbors[neighbor].append(city)

    q = deque([0])
    visited.add(0)
    while q:
        curr = q.popleft()
        for neighbor in neighbors[curr]:
            if neighbor not in visited:
                if (neighbor, curr) not in edges:
                    count += 1
                q.append(neighbor)
                visited.add(neighbor)

    return count


# This was really fun to solve, always remember that you only add the neighbors
# Time complexity will be O(n), space complexity O(n)
