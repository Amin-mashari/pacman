PAC_MAN = "p"
FOOD = "f"
WALL = "1"
SPACE = "0"

# read MAZE and print


def readMaze(filename):
    maze = []
    mazeFile = open(filename, "r")
    columns = mazeFile.readlines()
    for column in columns:
        column = column.strip()
        row = [i for i in column]
        maze.append(row)
    return maze
