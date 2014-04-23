# ----------
# User Instructions:
# 
# Define a function, search() that takes no input
# and returns a list
# in the form of [optimal path length, x, y]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1] # Make sure that the goal definition stays in the function.

delta = [[-1, 0 ], # go up
        [ 0, -1], # go left
        [ 1, 0 ], # go down
        [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

cost = 1

def search():
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    path =[0] + init
    openlist = []
    grid[path[1]][path[2]] = 1
    while path[1:]!=goal:
        # find unchecked neighbor
        for i in range(len(delta)):
            if path[1]+delta[i][0]< len(grid) and path[1]+delta[i][0] >= 0 and path[2]+delta[i][1]< len(grid[0]) and path[2]+delta[i][1] >= 0:
                #if this cell have not been checked
                if grid[path[1]+delta[i][0]][path[2]+delta[i][1]] != 0:
                    #check this cell
                    grid[path[1]+delta[i][0]][path[2]+delta[i][1]] = 0
                    #add to new open list
                    openlist.append([])
                    openlist[len(openlist)-1][0] = path[0]+1
                    openlist[len(openlist)-1][1] = path[1]+delta[i][0]
                    openlist[len(openlist)-1][2] = path[2]+delta[i][1]
                
    return path # you should RETURN your result

search()
