class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if grid is None : return 0 
        res = 0 
        n,m= len(grid), len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        visited = set()
        def bfs(a,b):
            queue = deque([(a,b)])
            visited.add((a,b))
            k=1
            while queue : 
                row,col = queue.popleft()
                for dr,dc in directions: 
                    nr = row +dr 
                    nc = col+ dc
                    if ( 0<= nr <n and 0<= nc <m and (nr,nc) not in visited and grid[nr][nc] == 1):
                        visited.add((nr,nc))
                        queue.append((nr,nc))
                        k+=1
            return k


        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and (i,j) not in visited : 
                    visited.add((i,j))
                    res= max(res,bfs(i,j))
        return res
