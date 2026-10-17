class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None : return 0
        rows= len(grid)
        cols= len(grid[0])
        visited= set()
        res=0
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        def bfs(startrow, startcol):
            queue = deque([(startrow,startcol)])
            visited.add((startrow,startcol))
            while queue: 
                row,col = queue.popleft()
                for dr,dc in directions: 
                    nr= row + dr
                    nc = col +dc
                    if (0<= nr < rows and 0<= nc < cols and grid[nr][nc]=="1" 
                    and (nr,nc) not in visited ):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        

        for row in range(rows): 
            for col in range(cols):
                if  grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row,col)
                    res +=1
        return res



        