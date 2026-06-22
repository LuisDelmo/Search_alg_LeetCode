import typing
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [(1,0),(-1,0),(0,1),(0,-1)]
        size_y = len(grid) - 1
        size_x = len(grid[0]) - 1
        islands = 0
        
        for y in range(size_y + 1):
            for x in range(size_x + 1):
                if grid[y][x] == "1":
                    queue = [(y,x)]
                    grid[y][x] = "0"
                    while queue:
                        curr_y,curr_x = queue.pop(0)
                        for m_y,m_x in moves:
                            new_y,new_x = (curr_y-m_y,curr_x-m_x)
                            if size_y >= new_y >= 0 and size_x >= new_x >= 0:
                                if grid[new_y][new_x] == "1":
                                    queue.append((new_y,new_x))
                                    grid[new_y][new_x] = "0"
                    islands += 1

        return islands
