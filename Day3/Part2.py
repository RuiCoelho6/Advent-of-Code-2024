import re

def parse_and_calculate_mul(pool):
    combined_pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    mul_enabled = True
    total = 0

    for match in re.finditer(combined_pattern, pool):
        if match.group(1) and match.group(2):
            if mul_enabled:
                x, y = int(match.group(1)), int(match.group(2))
                total += x * y
        elif match.group(0) == "do()":
            mul_enabled = True
        elif match.group(0) == "don't()":
            mul_enabled = False
    return (total)


with open("rep.txt", "r") as file:
    pool = file.read()
print(parse_and_calculate_mul(pool))
