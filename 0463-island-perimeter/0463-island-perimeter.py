class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            print(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result += 4
                    if i != len(grid) - 1 and grid[i+1][j] == 1 :
                        result -= 1
                    if i != 0 and grid[i-1][j] == 1:
                        result -= 1
                    if j != len(grid[i]) - 1 and grid[i][j+1] == 1:
                        result -= 1
                    if j != 0 and grid[i][j-1] == 1:
                        result -= 1
        return result