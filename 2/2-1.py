safe_sum = 0


def is_safe(line):
    data = line.split()
    data = list(map(int, data))

    if data[0] == data[1]:
        return False

    is_increasing = data[1] > data[0]

    for i in range(len(data) - 1):
        diff = data[i + 1] - data[i]

        if is_increasing:
            if diff <= 0 or diff > 3:
                return False
        else:
            if diff >= 0 or diff < -3:
                return False

    return True


with open("input", "r") as f:
    for line in f:
        if is_safe(line):
            safe_sum += 1

print(safe_sum)
