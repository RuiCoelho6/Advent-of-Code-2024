def read_grid(filename):
    result = []

    with open(filename, 'r') as file:
        for line in file:
            stripped_line = line.strip()
            char_list = list(stripped_line)
            result.append(char_list)
    return (result)

def find_xmas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    target = list("XMAS")
    occurrences = []

    directions = [
        (0, 1),
        (1, 0),
        (1, 1),
        (1, -1),
        (0, -1),
        (-1, 0),
        (-1, 1),
        (-1, -1)
    ]
    for start_row in range(rows):
        for start_col in range(cols):
            for d_row, d_col in directions:
                end_row = start_row + d_row * (len(target) - 1)
                end_col = start_col + d_col * (len(target) - 1)
                if (0 <= end_row < rows and 0 <= end_col < cols):
                    if all(grid[start_row + i*d_row][start_col + i*d_col] == target[i] 
                        for i in range(len(target))):
                        occurrences.append((start_row, start_col, d_row, d_col))

    return (occurrences)

grid = read_grid('rep.txt')
xmas_locations = find_xmas_occurrences(grid)
print(len(xmas_locations))