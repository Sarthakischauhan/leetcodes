class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Step 1: Build the graph
        edges = collections.defaultdict(list)

        for i in range(len(equations)):
            # ex a/b 
            edges[equations[i][0]].append({equations[i][1]: values[i]})
            edges[equations[i][1]].append({equations[i][0] : 1 / values[i]})

        def dfs(x,y,visited):



        return []

# Not working yet, can be done later
