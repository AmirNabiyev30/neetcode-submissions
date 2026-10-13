class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        With help
         we scan area and store infected in a queue,
        have 2 loops, outer for time and inner for infecting neigbors
        the length of inner loop will be the length of the queue at that time step


        Then we need to do final scan of the grid for fresh fruits
        """
        #create queue
        q = deque()
        #iterate through grid and store rotten in a queue
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    q.append([i,j])
        #iterate through grid, now we perform bfs 

        print(q)

        #define possible direction
        #.    down   up   right   left
        dr = [[1,0],[-1,0],[0,1], [0,-1]]

        #create an is_valid function
        def is_valid(i ,j):
            return 0<=i<len(grid) and 0<= j < len(grid[i])
        t = 0
        while q:
            qlen = len(q)
            print(q)
            for _ in range(qlen):
                i,j = q.popleft()
                for x,y in dr:

                    xpos,ypos = i+x,j+y
                    if not is_valid(xpos,ypos):
                        continue
                    #if it is a fresh fruit
                    if grid[xpos][ypos] == 1:
                        #we make it a rotten fruit and then add that fruit to the q
                        grid[xpos][ypos] = 2
                        q.append([xpos,ypos])
                    
            #increment time
            if len(q)>0:
                t = t+1
        #after done infecting
        #we do another scan to find fresh fruit
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return t
                    
                


        