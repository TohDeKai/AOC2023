def part1(puzzle):
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    res = 0
    cubesCount = {}
    for line in puzzle:
        line = line.split(":")
        game_num = int(line[0].replace("Game ", ""))
        games = line[1].split(";")
        exceed = False
        for game in games:
            cubes = game.split(",")
            cubesCount["red"] = cubesCount["blue"] = cubesCount["green"] = 0
            if exceed:
                break
            for i in range(len(cubes)):
                cubes[i] = cubes[i].strip().split(" ")
                [num, color] = cubes[i]
                cubesCount[color] += int(num)
                if (
                    cubesCount["red"] > 12
                    or cubesCount["green"] > 13
                    or cubesCount["blue"] > 14
                ):
                    exceed = True
                    break
        if not exceed:
            res += game_num
    return res


# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print("Part 1 Solution: " + str(part1(puzzle)))
