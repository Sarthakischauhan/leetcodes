class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        cc = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def connectedNeighbors(r, c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                # check side bounds and then check whether 1. Add to visited set. because you dequed, enqueue another value. 
                r, c = q.pop()
                moves = [[r+1,c+0], [r-1, c+0], [r+0, c+1], [r+0, c-1]]
                for v, h in moves:
                    if ( v in range(rows) and h in range(cols) and grid[v][h] == "1" and (v,h) not in visited):
                        q.append((v,h))
                        visited.add((v, h))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    # Check all neighbors and mark each of them visited if 1
                    connectedNeighbors(r,c)
                    cc += 1
        return cc

# Long time, here's the deal I tried this while under pressure of hw assignments.
# So I took help from neetcode. This solution is not mine except the syntatic sugar on line 16

