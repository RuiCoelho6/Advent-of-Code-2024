def convert_list_to_int(nbrs):
    new_nbrs = []
    for num in nbrs:
        new_nbrs.append(int(num))
    return new_nbrs

def is_sorted(nbrs):
    ascending = True
    descending = True

    for i in range(len(nbrs) - 1):
        if nbrs[i] > nbrs[i + 1]:
            ascending = False
        if nbrs[i] < nbrs[i + 1]:
            descending = False
    if ascending:
        return 0
    elif descending:
        return 1
    else:
        return 2

def count_safe_reports(file_path):
    counter = 0

    with open(file_path, 'r') as file:
        for line in file:
            nbrs = line.split()
            nbrs = convert_list_to_int(nbrs)
            if is_sorted(nbrs) in (0, 1):
                safe = True
                for i in range(len(nbrs) - 1):
                    if abs(nbrs[i] - nbrs[i + 1]) < 1 or abs(nbrs[i] - nbrs[i + 1]) > 3:
                        safe = False
                        break
                if safe:
                    counter += 1
    return counter

file_path = "reports.txt"
print(count_safe_reports(file_path))
