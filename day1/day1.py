def trebuchet_part1(puzzle):
    """
    1. need to iterate line by line
    2. find the first and last digit
    3. find the first digit by having a pointer starting at the start and iterating and stopping at first occurrence of a digit
    4. find the last digit by having a pointer starting at the end and iterating backwards and stopping at first occurrence of a digit
    5. take these 2 digits and combine it
    6. add this combined digits
    7. return
    """
    res = 0
    for line in puzzle:
        start, end = 0, len(line) - 1
        n = end
        while start < n:
            if line[start].isnumeric():
                first = line[start]
                break
            else:
                start += 1
        while end >= 0:
            if line[end].isnumeric():
                last = line[end]
                break
            else:
                end -= 1
        combined = first + last
        res += int(combined)
    return res


def trebuchet_part2(puzzle):
    """
    replace the digits with the numeric version then do part 1 again
    """
    # one two three four five six seven eight nine ten
    spelt_out_digits = {
        "one": "o1e",
        "two": "t2e",
        "three": "th3ee",
        "four": "f4ur",
        "five": "f5ve",
        "six": "s6x",
        "seven": "se7en",
        "eight": "ei8ht",
        "nine": "n9ne",
    }

    res = 0
    for line in puzzle:
        for key, value in spelt_out_digits.items():
            line = line.replace(key, value)

        start, end = 0, len(line) - 1
        n = end
        while start < n:
            if line[start].isnumeric():
                first = line[start]
                break
            else:
                start += 1
        while end >= 0:
            if line[end].isnumeric():
                last = line[end]
                break
            else:
                end -= 1
        combined = first + last
        res += int(combined)
    return res


# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print("Part 1 Solution: " + str(trebuchet_part1(puzzle)))
print("Part 2 Solution: " + str(trebuchet_part2(puzzle)))
