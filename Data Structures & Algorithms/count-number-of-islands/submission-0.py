class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Can we form a graph and find connections
        and from there figure it out
        lets simplify and find a smaller solution

        [0 0 0
         0 1 0
         0 0 0] == 1 island
        
        We basically propgate a message "infecting" neighbors
        """
        def is_valid(i,j) ->bool:
            return 0<= i < len(grid) and 0<= j < len(grid[i])
        #this will be our core logic of infecting islands
        def infect(i,j):
            #we want horizontal and vertical neighbors
            q = deque([(i,j)])
            #if right neighbor is unclaimed add to q
            while q:
                #pull the current val
                i, j = q.popleft()
                #infect current island
                grid[i][j] = "2"
                #join neighbors to queue
                #if right neighbor exists
                if is_valid(i+1,j) and grid[i+1][j] == "1":
                    q.append((i+1,j))
                if is_valid(i-1,j) and grid[i-1][j] == "1":
                    q.append((i-1,j))
                if is_valid(i,j+1) and grid[i][j+1] == "1":
                    q.append((i,j+1))
                if is_valid(i,j-1) and grid[i][j-1] == "1":
                    q.append((i,j-1))

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                #if we see a 1, we increment count and call and infect function
                if grid[row][col] == "1":
                    count+=1
                    infect(row,col)
        return count



        