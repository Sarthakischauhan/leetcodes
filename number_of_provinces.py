class Solution:
    def findCircleNum(self, arr: List[List[int]]) -> int:
        # Let's go with a DFS based solution. So we traverse through the adjacency list
        # Then we check current elements 
        n = len(arr)
        count = 0
        visited = []
        def dfs(neighbor):
            visited.append(neighbor)
            for i in range(n):
                if (arr[neighbor][i] == 1 and i not in visited):
                    dfs(i)

        for i in range(n):
            if (i not in visited):
                print(visited)
                dfs(i)
                count += 1 

        return count

# Depth first search, Time complexity O(n^2)
# Space complexity will be O(n)
