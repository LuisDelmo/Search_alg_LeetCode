import Typing
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        visited = set()
        minutes = 0
        rotten = [(y,x) for y in range(len(grid)) for x in range(len(grid[y])) if grid[y][x] == 2]
        queue.extend(rotten)
           
        while queue:
            to_rot = []
            for _ in range(len(queue)):
                y,x = queue.pop(0)
                visited.add((y,x))
                curr_neigh = find_neighbors(y,x,grid)

                for neigh_y,neigh_x in curr_neigh:
                    if (neigh_y,neigh_x) in visited:
                        continue
                    value_in_grid = grid[neigh_y][neigh_x]
                    if value_in_grid == 1:
                        to_rot.append((neigh_y,neigh_x))
                    else:
                        if (neigh_y,neigh_x) not in visited:
                            visited.add((neigh_y,neigh_x))
                            curr_neigh.extend(find_neighbors(neigh_y,neigh_x,grid))

            for t_y,t_x in to_rot:
                grid[t_y][t_x] = 2
            if to_rot:
                minutes += 1
            queue.extend(to_rot)

        if any(1 in row for row in grid):
            return -1
        return minutes


moves = [(1,0),(-1,0),(0,1),(0,-1)]
def find_neighbors(y,x,grid):
    size_y = len(grid)-1
    size_x = len(grid[0])-1
    neighbors = []
    for m_y,m_x in moves:
        new_y,new_x = (m_y+y,m_x+x)
        if size_y >= new_y >= 0 and size_x >= new_x >= 0:
            if grid[new_y][new_x] != 0:
                neighbors.append((new_y,new_x))
    return neighbors


                
