def is_xmas_tree(center_row, center_col):
    if not (1 <= center_row < total_rows - 1 and
            1 <= center_col < total_cols - 1):
        return (False)
    if grid[center_row][center_col] != "A":
        return (False)

    top_left_to_bottom_right = (
        grid[center_row - 1][center_col - 1] +
        grid[center_row + 1][center_col + 1])

    top_right_to_bottom_left = (
        grid[center_row - 1][center_col + 1] +
        grid[center_row + 1][center_col - 1])
    valid_diagonal_pairs = {"MS", "SM"}

    return (top_left_to_bottom_right in valid_diagonal_pairs and
        top_right_to_bottom_left in valid_diagonal_pairs)


with open("rep.txt") as file:
    grid = file.read().strip().split("\n")
total_rows = len(grid)
total_cols = len(grid[0])
xmas_tree_count = 0
for row in range(total_rows):
    for col in range(total_cols):
        if is_xmas_tree(row, col):
            xmas_tree_count += 1

print(xmas_tree_count)
