class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        hhi=False
        positionsOfOnes=[]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=="1":
                    positionsOfOnes.append((i,j))

        def dfs(i, j):
            if (i < 0 or i >= len(grid) or 
                j < 0 or j >= len(grid[0]) or 
                grid[i][j] != "1"):
                return
            grid[i][j] = "0"  # mark visited
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        islandCount = 0
        for i, j in positionsOfOnes:
            if grid[i][j] == "1":
                islandCount += 1
                dfs(i, j)
        return islandCount
        

        
sol=Solution().numIslands
grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(sol(grid))
print(sol(grid2))