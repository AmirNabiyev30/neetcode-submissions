class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #initalize
        grid = [[0]*m for _ in range(n)]
        
        
        for i in range (m):
            grid[0][i] = 1
        for j in range(n):
            grid[j][0] = 1
        #now we can do our algorithmn, one row at a time we increment
        for row in range(1,n):
            for col in range(1,m):
                grid[row][col] = grid[row-1][col]+grid[row][col-1]
        
        return grid[-1][-1]
        