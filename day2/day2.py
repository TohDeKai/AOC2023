def part1(puzzle):
    # 12 red cubes, 13 green cubes, and 14 blue cubes
    red, green, blue = 12, 13, 14
    res = 0
    for line in puzzle:
        line = line.split(":")
        game_num = int(line[0].replace("Game ", ""))
        games = line[1].split(";")
        exceed = False
        for game in games:
            cubes = game.split(",")
            red = green = blue = 0
            if exceed:
                break
            for i in range(len(cubes)):
                cubes[i] = cubes[i].strip().split(" ")
                num = cubes[i][0]
                color = cubes[i][1]
                if color == "red":
                    red += int(num)
                elif color == "green":
                    green += int(num)
                else:
                    blue += int(num)
                if red > 12 or green > 13 or blue > 14:
                    exceed = True
                    break
        if not exceed:
            res += game_num

    return res


# reading input
with open("input.txt") as f:
    puzzle = f.readlines()

print("Part 1 Solution: " + str(part1(puzzle)))
