class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #im thinking we can do something similar to rotten oranges,
        """
        find all treasue chests, store them in a queue
        and then perform a layered BFS that modifies in place based on outer loop
        """
        #intialize q 
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    q.append([i,j]) # append pos of treasure

        #bfs of treasure
        print(q)
        def is_valid(i,j):
            return 0<= i < len(grid) and 0<= j <len(grid[i])
        dr = [[-1,0], [1,0],[0,1],[0,-1]]
        dist = 1
        while q:
            qlen = len(q)
            for _ in range(qlen):
                i,j = q.popleft()
                for x,y in dr:
                    xpos, ypos = i+x,j+y
                    if not is_valid(xpos,ypos):
                        continue
                    if grid[xpos][ypos] > 0 and dist < grid[xpos][ypos]:
                        grid[xpos][ypos] = dist
                        q.append([xpos,ypos])
            dist+=1
                        
                

        