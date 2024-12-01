def separate_numbers(file_path):
    first_column = []
    second_column = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                numbers = line.split()
                first_column.append(int(numbers[0]))
                second_column.append(int(numbers[1]))

        first_column = sorted(first_column)
        second_column = sorted(second_column)
        return (first_column, second_column)

    except FileNotFoundError:
        return (None)

def get_diff(first_column, second_column):
    diff_nbrs = []

    for first_nbr, second_nbr in zip(first_column, second_column):
        diff_nbrs.append(int(abs(first_nbr - second_nbr)))
    return (diff_nbrs)

file_path = "input.txt"
result = separate_numbers(file_path)
if result is None:
    print("Error: File ", file_path, " not found")
else:
    first_column, second_column = result
    diff_nbrs = get_diff(first_column, second_column)
    print(sum(diff_nbrs))

