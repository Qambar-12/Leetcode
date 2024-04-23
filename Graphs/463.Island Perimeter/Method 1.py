def islandPerimeter(grid):
    perimeter = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if r == 0:
                if c == 0:
                    if grid[r][c]:
                        perimeter += 4
                else: 
                    if grid[r][c]:
                        if grid[r][c-1]:
                            perimeter += (3-1)
                        else:
                            perimeter += 4

            else:
                if c == 0:
                    if grid[r][c]:
                        if grid[r-1][c]:
                            perimeter += (3-1)
                        else:
                            perimeter += 4
                else:
                    if grid[r][c]:
                        if grid[r-1][c] and grid[r][c-1]:
                            perimeter += (2-2)
                        elif grid[r-1][c] or grid[r][c-1]:
                            perimeter += (3-1)
                        else:
                            perimeter += 4
    return perimeter                        

print(islandPerimeter([[1,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,1,1]]))
                                        