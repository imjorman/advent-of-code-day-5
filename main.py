def part_1():
    GRID_SIZE = 1000

    # Make the grid
    row = []
    box = []
    for i in range(GRID_SIZE):
        row.append(".")
    for c in range(GRID_SIZE):
        box.append(list(row))

    with open("day-5-input.txt") as file:
        lines = file.readlines()

    codes = []
    for line in lines:
        codes.append(line.split("->"))

    list_of_codes = []
    for code in range(len(codes)):
        for item in range(len(codes[code])):
            list_of_codes.append(codes[code][item].split(","))

    pairs = []
    for item in range(0, len(list_of_codes), 2):
        added_list = list_of_codes[item] + list_of_codes[item + 1]
        pairs.append(added_list)

    for segment in pairs:
        starting_x = int(segment[0])
        starting_y = int(segment[1])
        ending_x = int(segment[2])
        ending_y = int(segment[3])

        if starting_x == ending_x and starting_y != ending_y:
            if box[starting_y][starting_x] == ".":
                box[starting_y][starting_x] = 1
            else:
                box[starting_y][starting_x] += 1

            if starting_y > ending_y:
                difference = starting_y - ending_y

                for counter in range(1, difference + 1):
                    new_coord = starting_y - counter
                    if box[new_coord][starting_x] == ".":
                        box[new_coord][starting_x] = 1
                    else:
                        box[new_coord][starting_x] += 1
            else:
                difference = ending_y - starting_y

                for counter in range(1, difference + 1):
                    new_coord = starting_y + counter
                    if box[new_coord][starting_x] == ".":
                        box[new_coord][starting_x] = 1
                    else:
                        box[new_coord][starting_x] += 1

        elif starting_y == ending_y and starting_x != ending_x:
            if box[starting_y][starting_x] == ".":
                box[starting_y][starting_x] = 1
            else:
                box[starting_y][starting_x] += 1

            if starting_x > ending_x:
                difference = starting_x - ending_x

                for counter in range(1, difference + 1):
                    new_coord = starting_x - counter
                    if box[starting_y][new_coord] == ".":
                        box[starting_y][new_coord] = 1
                    else:
                        box[starting_y][new_coord] += 1
            else:
                difference = ending_x - starting_x

                for counter in range(1, difference + 1):
                    new_coord = starting_x + counter
                    if box[starting_y][new_coord] == ".":
                        box[starting_y][new_coord] = 1
                    else:
                        box[starting_y][new_coord] += 1
        else:
            if box[starting_y][starting_x] == ".":
                box[starting_y][starting_x] = 1
            else:
                box[starting_y][starting_x] += 1

            if starting_x > ending_x:
                pass
                difference = starting_x - ending_x

                for counter in range(1, difference + 1):
                    new_x_coord = starting_x - counter
                    new_y_coord = starting_y
                    if starting_y > ending_y:
                        new_y_coord -= counter
                    else:
                        new_y_coord += counter

                    if box[new_y_coord][new_x_coord] == ".":
                        box[new_y_coord][new_x_coord] = 1
                    else:
                        box[new_y_coord][new_x_coord] += 1
            else:
                difference = ending_x - starting_x
                for counter in range(1, difference + 1):
                    new_x_coord = starting_x + counter
                    new_y_coord = starting_y

                    if starting_y > ending_y:
                        new_y_coord -= counter
                    else:
                        new_y_coord += counter

                    if box[new_y_coord][new_x_coord] == ".":
                        box[new_y_coord][new_x_coord] = 1
                    else:
                        box[new_y_coord][new_x_coord] += 1


    score = 0
    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            if box[row][column] == "." or box[row][column] == 1:
                pass
            else:
                score += 1

    print(score)

part_1()
