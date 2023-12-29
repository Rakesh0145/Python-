#Given a binary 2D matrix, find the number of islands. A group of connected 1's forms an island.

#Test Case:

#Input: mat[][] = {{1, 1, 0, 0, 0},                            

                             #    {0, 1, 0, 0, 1},                            

                             #    {1, 0, 0, 1, 1},                           

                             #    {0, 0, 0, 0, 0},                          

                             #   {1, 0, 1, 0, 0}

                              # } 

#Output: 4



def numIslands(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    count = 0

    def dfs(row, col):
        if 0 <= row < rows and 0 <= col < cols and matrix[row][col] == 1:
            matrix[row][col] = 0  # Mark the current cell as visited
            # Explore neighbors in all directions
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 1:
                count += 1
                dfs(row, col)

    return count

# Test case
matrix = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0]
]

result = numIslands(matrix)
print(result)
