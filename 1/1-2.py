count_dict = {}

# Read input into left and right list
with open("input", "r") as f:
    for line in f:
        left, right = line.split()
        if right in count_dict:
            count_dict[right] += 1
        else:
            count_dict[right] = 1

res = 0
with open("input", "r") as f:
    for line in f:
        left, right = line.split()
        if left in count_dict:
            res += count_dict[left] * int(left)

print(res)
