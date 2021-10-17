from random import randrange, shuffle

AGENT = "p"
FOOD = "f"
WALL = "1"
SPACE = "0"
maze_folder = "maps//"


def readMaze(filename):
    maze = []
    mazeFile = open(maze_folder + filename, "r")
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


def generate_maze(w=16, h=8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["100"] * w + ['1'] for _ in range(h)] + [[]]
    hor = [["111"] * w + ['1'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "100"
            if yy == y:
                ver[y][max(x, xx)] = "000"
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


def save_maze(row, column, filename):

    maze = generate_maze(row, column)
    text_file = open((maze_folder + filename), "w")
    text_file.write(maze)
    text_file.close()


maze = readMaze("map2.txt")
