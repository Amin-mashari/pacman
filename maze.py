AGENT = "p"
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


def getAgentPosition(maze):

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if(maze[i][j] == AGENT):
                agent = [i, j]
            if(maze[i][j] == FOOD):
                food = [i, j]

    maze[agent[0]][agent[1]] = SPACE
    maze[food[0]][food[1]] = SPACE
    return agent, food


maze = readMaze("map01.txt")
