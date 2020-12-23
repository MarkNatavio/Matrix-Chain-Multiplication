import sys

def displayGrid(grid, dimensions):
    for i in range(1, dimensions):
        print("|"),
        for j in range (1, dimensions):
            print(grid[i][j]),
        
        print("|")

def MatrixChainMulti(grid,dimensions,P):
    m = grid
    for i in range (dimensions):
        m[i][i] = 0
        
    for l in range (2,dimensions):
        for i in range (1,dimensions-l+1):
            j = i+l-1
            s = []
            ans = []
            print("Finding m["+str(i)+","+str(j)+"]")
            for k in range (i,j):
                q = m[i][k]+m[k+1][j]+(P[i-1]*P[k]*P[j])
                print("m[i,j] = "+str(m[i][k])+" + "+str(m[k+1][j])+" + ("+str(P[i-1])+"*"+str(P[k])+"*"+str(P[j])+") = "+str(m[i][k]+m[k+1][j])+" + "+str(P[i-1]*P[k]*P[j])+" = "+str(q)+", k = "+str(k))
                s.append(k)
                ans.append(q)
            
            print("The minimum is "+str(min(ans))+" at k = "+str(s[ans.index(min(ans))]))
            print("============================================")
            print("")
            m[i][j] = min(ans)
            
    displayGrid(m,dimensions)
    

print("m[i,j] = m[i,k]+m[k+1,j]+P[i-1]*P[k]*P[j]")
print("")
P = [30,35,15,5]

dimensions = len(P)

# set the grid
grid = []
for i in range(dimensions):
    row = []
    for j in range(dimensions):
        row.append(0)
    grid.append(row)

MatrixChainMulti(grid,dimensions,P)