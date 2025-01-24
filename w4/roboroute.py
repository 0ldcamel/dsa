import time

def analyze_route(grid):
    if grid == ["R"]:
        return (1, True)
    gridmap = make_grid(grid)
    direction = "north"
    robot_row, robot_col =  find_robot(gridmap)
    # print_gridmap(gridmap)
    # sleep = 0.2
    # time.sleep(sleep)
    loop_check = []
    breadcrumbs = set()
    while True:
        breadcrumbs.add((robot_row, robot_col))
        try: 
            if check_front(gridmap, robot_row, robot_col, direction):
                robot_row, robot_col = robot_move(gridmap, robot_row, robot_col, direction)
                if (robot_row, robot_col, direction) in loop_check:
                    return len(breadcrumbs), False
                else:
                    breadcrumbs.add((robot_row, robot_col))
                    loop_check.append((robot_row, robot_col, direction))
                # print_gridmap(gridmap)
                # time.sleep(sleep)
            else:
                direction = turn_right(direction)
                if (robot_row, robot_col, direction) in loop_check:
                    return len(breadcrumbs), False
                else:
                    breadcrumbs.add((robot_row, robot_col))
                    loop_check.append((robot_row, robot_col, direction))
        except IndexError:
            return len(breadcrumbs), True

def turn_right(direction):
    directions =["north", "east", "south", "west"]
    direction_index = directions.index(direction)
    new_index = (direction_index + 1) % 4
    return directions[new_index]


def check_front(gridmap, robot_row, robot_col, direction):
    directions = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
    del_row, del_col = directions[direction][0], directions[direction][1]
    if robot_row + del_row >= 0 and robot_col + del_col >= 0:
        return gridmap[robot_row + del_row][robot_col + del_col] != "#"
    raise IndexError

def robot_move(gridmap, robot_row, robot_col, direction):
    directions = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
    del_row, del_col = directions[direction][0], directions[direction][1]
    gridmap[robot_row][robot_col] = "."
    robot_row += del_row
    robot_col += del_col
    gridmap[robot_row][robot_col] = "R"
    return robot_row, robot_col


def find_robot(grid):
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "R":
                return row, col

def make_grid(grid):
    gridmap = []
    for row in grid:
        maprow = []
        for char in row:
            maprow.append(char)
        gridmap.append(maprow)
    return gridmap

def print_gridmap(gridmap):
    for row in gridmap:
        print("".join(row))
    print()

if __name__ == "__main__":
    grid1 = [".#......",
             "..#.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid1)) # (14, True)

    # time.sleep(1)

    grid2 = ["........",
             ".##.....",
             ".......#",
             "#.R.....",
             "......#."]
    print(analyze_route(grid2)) # (12, False)


    # grid3 = ["........",
    #          ".##.....",
    #          ".......#",
    #          ".......#",
    #          ".......#",
    #          ".......#",
    #          ".......#",
    #          "#.R.....",
    #          "......#."]
    # print(analyze_route(grid3)) # (12, False)

    grid4 = ["###",
             "#R#",
             ".##"]
    
    print(analyze_route(grid4))
