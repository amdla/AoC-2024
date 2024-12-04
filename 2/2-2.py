safe_sum = 0


def is_safe(line, try_remove_next):
    """
    Check if the sequence in the line is safe.
    Try removing the current (`try_remove_next=False`) or the next (`try_remove_next=True`) element if necessary.
    """
    data = list(map(int, line.split()))
    fix_available = True

    if len(data) < 2:  # Ensure there are at least two elements
        return False

    if data[0] == data[1]:  # Handle equal first elements
        data.pop(0)
        fix_available = False

    is_increasing = data[1] > data[0]

    i = 0
    while i < len(data) - 1:
        diff = data[i + 1] - data[i]

        if is_increasing:
            if diff <= 0 or diff > 3:  # Invalid increasing condition
                if fix_available:
                    if try_remove_next:
                        data.pop(i + 1)  # Remove the next element
                    else:
                        data.pop(i)  # Remove the current element
                    fix_available = False
                    i = 0  # Restart the loop
                    continue
                else:
                    return False
        else:
            if diff >= 0 or diff < -3:  # Invalid decreasing condition
                if fix_available:
                    if try_remove_next:
                        data.pop(i + 1)  # Remove the next element
                    else:
                        data.pop(i)  # Remove the current element
                    fix_available = False
                    i = 0  # Restart the loop
                    continue
                else:
                    return False

        i += 1  # Move to the next pair

    return True


# Process the input file
with open("input", "r") as f:
    for line in f:
        if is_safe(line, False):  # Try removing the current element first
            safe_sum += 1
        elif is_safe(line, True):  # If that fails, try removing the next element
            safe_sum += 1

print(safe_sum)
