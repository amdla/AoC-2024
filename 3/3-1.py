import re

# Define the regex pattern
pattern = r"mul\((-?\d+),\s*(-?\d+)\)"

res = 0
with open("input", "r") as f:
    lines = f.readlines()
    for line in lines:
        matches = re.findall(pattern, line)

        for match in matches:
            print(match)

            num1 = int(match[0])
            num2 = int(match[1])
            res += num1 * num2

print(res)
