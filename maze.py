from random import randrange, shuffle
import random

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
    print(maze)
    return maze


def getAgentAndFoodPossRandomly(maze):

    while True:
        agent_poss_x = randrange(1 , len(maze) - 1)
        agent_poss_y = randrange(1 , len(maze[agent_poss_x]) - 1)

        if(maze[agent_poss_x][agent_poss_y] == SPACE):
            break

    while True:
        food_poss_x = randrange(1 , len(maze) - 1)
        food_poss_y = randrange(1 , len(maze[food_poss_x]) - 1)

        if(maze[food_poss_x][food_poss_y] == SPACE):
            if not( food_poss_x == agent_poss_x and food_poss_y == agent_poss_y):
                break

    agent = [agent_poss_x , agent_poss_y]
    food = [food_poss_x , food_poss_y]
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
    print(maze)
    text_file = open((maze_folder + filename), "w")
    text_file.write(maze)
    text_file.close()


maze = readMaze("map1.txt")
