import re

def parse_and_calculate_mul(pool):
    total = 0
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    mul_matches = re.findall(mul_pattern, pool)
    for x, y in mul_matches:
        total += int(x) * int(y)
    return (total)

with open("rep.txt", "r") as file:
    pool = file.read()
print(parse_and_calculate_mul(pool))