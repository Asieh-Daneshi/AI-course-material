import numpy as np
import pandas as pd
# =============================================================================
mazeText=pd.read_csv('maze2.txt',header=None)
Maze = np.empty([np.size(mazeText,0),len(mazeText.iloc[0,0])])
n=1
for a1 in np.arange(0,np.size(mazeText,0)):
    temp=mazeText.iloc[a1,0]
    for a2 in np.arange(0,len(mazeText.iloc[0,0])):
        if temp[a2]=='#':                                             # blocked
            Maze[a1,a2]=0
        elif temp[a2]==' ':                                              # path
            Maze[a1,a2]=n
            n=n+1
        elif temp[a2]=='A':                                             # start 
            Maze[a1,a2]=-1
        else:                                                             # end
            Maze[a1,a2]=-2
# This function finds neighbors of input element (up, down, right, left) elements
def get_neighbors(matrix, row, col):
    rows, cols = len(matrix), len(matrix[0])            # Get matrix dimensions
    neighbors = []

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]     # Up, Down, Left, Right

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols:      # Check boundaries
            neighbors.append(matrix[new_row][new_col])

    return neighbors

# =============================================================================
Frontiers = []
Seen = []
Frontiers.append(-1)                 # find start point
endPoint = -2
# Frontiers.append(list(np.where(Maze == -1)))                 # find start point
# endPoint=list(np.where(Maze == -2))
n=0
# while(Frontiers[n]!=endPoint):

while(len(np.setdiff1d(Frontiers, Seen))>0 and Frontiers[n]!=endPoint):
        Seen.append(Frontiers[n])
        Neighbors=get_neighbors(Maze, list(np.where(Maze == Frontiers[n]))[0][0],list(np.where(Maze == Frontiers[n]))[1][0])
        m=0
        n=n+1
        for a1 in np.arange(0,len(Neighbors)):
            if ((Neighbors[a1]!=0) and (Neighbors[a1] not in Frontiers)):
                # if (Neighbors[a1]!=endPoint):
                    m=m+1
                    Frontiers.append(Neighbors[a1])
                    print(n)
                    if m>1:
                        n=n-1
                    
Solution=Maze
for a1 in np.arange(0,np.size(Maze,0)):
    for a2 in np.arange(0,np.size(Maze,1)):
        if Maze[a1,a2] in Seen:
            Solution[a1,a2]=8
        elif Maze[a1,a2]!=0:
            Solution[a1,a2]=1
    
            