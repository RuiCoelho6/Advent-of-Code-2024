def separate_numbers(file_path):
    first_column = []
    second_column = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                numbers = line.split()
                first_column.append(int(numbers[0]))
                second_column.append(int(numbers[1]))
        return (first_column, second_column)

    except FileNotFoundError:
        return (None)

def sim_score(first_column, second_column):
    result = []

    for num in first_column:
        count = second_column.count(num)
        result.append(num * count)
    return (result)

file_path = "input.txt"
result = separate_numbers(file_path)
if result is None:
    print("Error: File ", file_path, " not found")
else:
    first_column, second_column = result
    sim_nbrs = sim_score(first_column, second_column)
    print(sum(sim_nbrs))
