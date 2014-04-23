# ----------
# User Instructions:
# 
# Create a function compute_value() which returns
# a grid of values. Value is defined as the minimum
# number of moves required to get from a cell to the
# goal. 
#
# If it is impossible to reach the goal from a cell
# you should assign that cell a value of 99.

# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']
cost = 1
cost_step = 1 # the cost associated with moving from a cell to an adjacent one.

# ----------------------------------------
# insert code below
# ----------------------------------------
def search(init, goal):
    # ----------------------------------------
    # insert code here and make sure it returns the appropriate result
    # ----------------------------------------
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    count = 0
    path =[0] + init
    openlist = []
    #check the first cell
    closed[path[1]][path[2]] = 1
    expand[path[1]][path[2]] = 0
    while True:#path[1:]!=goal:
        #search for the neighbor
        for i in range(len(delta)):
            if path[1]+delta[i][0]< len(grid) and path[1]+delta[i][0] >= 0 and path[2]+delta[i][1]< len(grid[0]) and path[2]+delta[i][1] >= 0:
                #if this cell have not been checked
                if grid[path[1]+delta[i][0]][path[2]+delta[i][1]] != 1 and closed[path[1]+delta[i][0]][path[2]+delta[i][1]] != 1:
                    #check this cell
                    closed[path[1]+delta[i][0]][path[2]+delta[i][1]] = 1
                    #add to new open list
                    openlist.append([])
                    openlist[len(openlist)-1].append(path[0]+1)
                    openlist[len(openlist)-1].append(path[1]+delta[i][0])
                    openlist[len(openlist)-1].append(path[2]+delta[i][1])
                    expand[path[1]+delta[i][0]][path[2]+delta[i][1]] = path[0]+1
                    count += 1
        #find the smallest g-value
        if len(openlist)!=0:            
            openlist = sorted(openlist,key=lambda l:l[0], reverse=False)
            path = openlist[0]
            openlist.pop(0)
        else:
            break    
    for i in range(len(expand)):
        print expand[i]
    return expand

def compute_value():
    #value = [[99 for row in range(len(grid[0]))] for col in range(len(grid))]
    value = search([len(grid)-1, len(grid[0])-1],[0,0])
                
    for i in range(len(value)):
        for j in range(len(value[0])):
            if value[i][j] == -1:
                value[i][j] = 99
             
        
    return value #make sure your function returns a grid of values as demonstrated in the previous video.

compute_value()

