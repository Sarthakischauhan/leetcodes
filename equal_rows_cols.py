class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = {}
        rows = {}
        n = len(grid)
        count = 0 
        for i in range(n):
            rows[i] = "-".join(map(str,grid[i]))
            col = ""
            for j in range(n):
                col += str(grid[j][i]) + "-"
            cols[i] = col[:-1]
        print(rows)
        print(cols)
        # Now check whether any string matches.
        for i in range(n):
            for j in range(n):
                if ( rows[i] == cols[j]):
                    count += 1
        return count


# Brute force solution, pretty sure there is a better way of solving these
# Time complexity -> O(n^2)
# Space complexity -> O(n^2)
