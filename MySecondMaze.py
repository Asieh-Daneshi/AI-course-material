#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""
Created on Thu Feb 27 21:59:10 2025

@author: Asieh Daneshi
This code solves a maze fed to the code as a text file in line 15. 'A' represents
the start point, 'B' represents the goal, and '#' shows blocked paths.
"""
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import numpy as np
import pandas as pd

# =============================================================================
# Load and Convert Maze File
mazeText = pd.read_csv('maze2.txt', header=None)
rows, cols = np.size(mazeText, 0), len(mazeText.iloc[0, 0])
Maze = np.empty((rows, cols), dtype=int)

# Parse the maze and assign numeric values
start = None
goal = None

for r in range(rows):
    temp = mazeText.iloc[r, 0]
    for c in range(cols):
        if temp[c] == '#':  # Wall
            Maze[r, c] = 0
        elif temp[c] == ' ':  # Open path
            Maze[r, c] = 1
        elif temp[c] == 'A':  # Start
            Maze[r, c] = -1
            start = (r, c)
        elif temp[c] == 'B':  # Goal
            Maze[r, c] = -2
            goal = (r, c)

# =============================================================================
# Function to find neighbors (valid moves)
def get_neighbors(matrix, row, col):
    rows, cols = matrix.shape
    neighbors = []

    # Directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and matrix[nr, nc] != 0:
            neighbors.append((nr, nc))  # Store valid coordinate pairs

    return neighbors

# =============================================================================
# Depth-First Search (DFS) to find the path
def solve_maze_dfs(maze, start, goal):
    # if start is None or goal is None:
    #     return None  # Invalid maze

    stack = [(start, [start])]  # (current_position, path_taken)
    visited = set()

    while stack:
        print(stack)
        (row, col), path = stack.pop()      # put the last element of stack in "(row, col), path"

        if (row, col) == goal:  # Goal reached
            return path

        if (row, col) not in visited:
            visited.add((row, col))

        for neighbor in get_neighbors(maze, row, col):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None  # No solution found

# =============================================================================
# Solve the maze and print the path
path = solve_maze_dfs(Maze, start, goal)
print("Correct Path:", path)