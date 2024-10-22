class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        edges = collections.defaultdict(dict)
        for i in range(len(equations)):
            a,b = equations[i]
            edges[a][b] = values[i]
            edges[b][a] = 1 / values[i]

        print(edges)  

        def DFS(start, end, visited):
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor in edges[start]:
                if neighbor not in visited:
                    res = DFS(neighbor, end, visited)
                    if res != -1.0:
                        return res * edges[start][neighbor]
            return -1.0

        results = []
        for start, end in queries:
            if start in edges and end in edges:
                visited = set()
                results.append(DFS(start,end,visited))
            else:
                results.append(-1.0)
        return results

# I didn't exactly figure out how to implement graph in code, I always seem to forget the algos
