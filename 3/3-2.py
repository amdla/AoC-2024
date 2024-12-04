import re

# Define the regex pattern to match 'mul()', 'do()', and 'don't()'
pattern = r"(mul\((-?\d+),\s*(-?\d+)\))|(do\(\))|(don't\(\))"

res = 0
flag = True

with open("input", "r") as f:
    lines = f.readlines()

    # Loop through each line
    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:

            if match[0]:  # If 'mul()' match
                if flag:
                    res += int(match[1]) * int(match[2])
                print(f"mul() matched with numbers: {match[1]}, {match[2]} and flag is set to {flag}")
                print(f"current result is {res}")
            elif match[3]:
                flag = True
                print("set flag to True")
            elif match[4]:
                flag = False
                print("set flag to False")

print(res)
