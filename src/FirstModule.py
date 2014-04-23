colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]

#DO NOT USE IMPORT
#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT
#[0,1]    right
#[1,0]    down
p_undershoot = (1.-p_move)
p_overshoot = 0

def sense(mat, Z):
    q=copy2dList(mat)
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            hit = (Z == colors[i][j])
            q[i][j] = (mat[i][j] * (hit * sensor_right + (1-hit) * (1-sensor_right)))
    s = sum(map(sum, q))
    for i in range(len(q)):
        for j in range(len(q[0])):
            q[i][j] = q[i][j] / s

    return q

def move(mat, U):
    q = copy2dList(mat)
    if(U[0] == 0 and U[1] != 0):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                q[i][j] = mat[i][j-U[1]+1]*p_undershoot+mat[i][(j-U[1])% len(mat[0])]*p_move+mat[i][(j-U[1]-1)% len(mat[0])]*p_overshoot
    elif(U[1] == 0 and U[0] != 0):
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                q[i][j] = mat[i-U[0]+1][j]*p_undershoot+mat[(i-U[0])% len(mat)][j]*p_move+mat[(i-U[0]-1)% len(mat)][j]*p_overshoot
    
    return q

def copy2dList(inlist):
    retlist = []
    for i in range(len(inlist)):
        retlist.append([])
        for j in range(len(inlist[0])):
            retlist[i].append(inlist[i][j])

    return retlist
            

p = []
numberofCells = len(colors)*len(colors[0])
normalizedValue = 1./numberofCells
onerow = []
#construct a normalized p matrix
for i in range(len(colors[0])):
        onerow.append(normalizedValue)

for i in range(len(colors)):
        p.append(onerow)

 
for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, measurements[k])
    
# print p


#Your probability array must be printed 
#with the following code.

show(p)


