def part1(puzzle):
    # 12 red cubes, 13 green cubes, and 14 blue cubes

    """
    ur curr sol is wrong because it doesn't account for if no red or no green
    """
    red, green, blue = 12, 13, 14
    res = 0
    for line in puzzle:
        line = line.split(":")
        game_num = line[0].replace("Game ", "")
        games = line[1].split(";")
        for game in games:
            cubes = game.split(",")
            for i in range(3):
                cubes[i] = cubes[i].replace("red", "")
                cubes[i] = cubes[i].replace("green", "")
                cubes[i] = cubes[i].replace("blue", "")
                cubes[i] = cubes[i].strip()
                cubes[i] = int(cubes[i])
                print(cubes[i])
            if cubes[0] > red or cubes[1] > green or cubes[2] > blue:
                continue
            else:
                res += game_num
    return res


# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print("Part 1 Solution: " + str(part1(puzzle)))
