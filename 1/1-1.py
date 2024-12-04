left_list = []
right_list = []

# Read input into left and right list
with open("input", "r") as f:
    for line in f:
        left, right = line.split()
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

res = 0
for left, right in zip(left_list, right_list):
    res += abs(int(right) - int(left))

print(res)
