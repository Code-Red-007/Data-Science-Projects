# Define a function that takes a 2D list of characters as input
def count_adjacent_mines(grid):
    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Create a new 2D list with the same dimensions as the input grid,
    # initialized with zeros for each cell
    new_grid = [[0 for j in range(cols)] for i in range(rows)]

    # Iterate over each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # Check if the current cell is an empty cell ("-")
            if grid[i][j] == "-":
                count = 0
                # Iterate over each adjacent cell (including diagonals) to the current cell
                for x in range(max(0, i-1), min(rows, i+2)):
                    for y in range(max(0, j-1), min(cols, j+2)):
                        # If the adjacent cell contains a mine, increment the count
                        if grid[x][y] == "#":
                            count += 1
                # Store the count in the corresponding cell of the new grid
                new_grid[i][j] = count
            else:
                # If the current cell is already a mine, simply copy it to the new grid
                new_grid[i][j] = grid[i][j]

    # Return the new grid
    return new_grid

# Create a sample grid for testing the function
grid = [
    ['#', '-', '-', '#', '-'],
    ['-', '-', '-', '-', '-'],
    ['-', '#', '-', '-', '-'],
    ['-', '-', '-', '#', '-'],
    ['-', '-', '-', '-', '-']
]

# Apply the count_adjacent_mines function to the sample grid and print the resulting new grid
new_grid = count_adjacent_mines(grid)
for row in new_grid:
    print(' '.join(str(cell) for cell in row))

    # end of program
