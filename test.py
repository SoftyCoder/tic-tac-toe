

grid = [1, 1, 1, 
        0, 0, 0,
        0, 0, 0]


def did_anyone_win():
    won = False
    #vertical
    for j in range(3):
        if (grid[j] == grid[j+3]) and (grid[j]!=0):
            if grid[j+3] == grid[j+6]:
                won = True
                who_won = grid[j]
                break
            
    i = 0
    while i <= 6:
        if (grid[i] == grid[i+1]) and (grid[i]!=0):
            if grid[i+1] == grid[i+2]:
                won = True
                who_won = grid[i]
                break
        
        i += 3
    return won


print(did_anyone_win())