from random import randrange, shuffle

AGENT = "a"
FOOD = "f"
WALL = "*"
SPACE = "-"
maze_folder = "envirements//"
agent_poss = [-1, -1]
food_poss = [-1, -1]


def readMaze(filename):
    maze = []
    mazeFile = open(maze_folder + filename, "r")
    columns = mazeFile.readlines()
    x = 0
    for column in columns:
        column = column.strip()
        row = [i for i in column]
        maze.append(row)
        y = 0
        for i in row:
            if(i == AGENT):
                agent_poss[0] = x
                agent_poss[1] = y

            elif(i == FOOD):
                food_poss[0] = x
                food_poss[1] = y
            y += 1
        x += 1
    return maze


def generate_maze(w=16, h=8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["*--"] * w + ['*'] for _ in range(h)] + [[]]
    hor = [["***"] * w + ['*'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "*--"
            if yy == y:
                ver[y][max(x, xx)] = "---"
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = f'{w},{h}'
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


def save_maze(filename):

    row, column = input("insert m , n")
    maze = generate_maze(row, column)
    print(maze)
    text_file = open((maze_folder + filename), "w")
    text_file.write(maze)
    text_file.close()
    return maze


class MAZE:

    def __init__(self, filename):
        try:
            self.maze = readMaze(filename)
        except:
            self.maze = save_maze(filename)

    def init_food_and_agent_poss_in_maze(this, agent_p, food_p):
        this.maze[agent_p[0]][agent_p[1]] = AGENT
        this.maze[food_p[0]][food_p[1]] = FOOD

    def get_agent_and_food_poss_from_file(self):
        if(agent_poss[0] == -1):
            agent_p, food_p = self.getAgentAndFoodPossRandomly()
            self.init_food_and_agent_poss_in_maze(agent_p, food_p)
            return agent_p, food_p
        else:
            return agent_poss, food_poss

    def getAgentPossRandomly(this):

        while True:
            agent_poss_x = randrange(1, len(this.maze) - 1)
            agent_poss_y = randrange(1, len(this.maze[agent_poss_x]) - 1)

            if(this.maze[agent_poss_x][agent_poss_y] == SPACE):
                break

        return [agent_poss_x, agent_poss_y]

    def getAgentAndFoodPossRandomly(self, this):
        agent = self.getAgentPossRandomly(this.maze)

        while True:
            food_poss_x = randrange(1, len(this.maze) - 1)
            food_poss_y = randrange(1, len(this.maze[food_poss_x]) - 1)

            if(this.maze[food_poss_x][food_poss_y] == SPACE):
                if not(food_poss_x == agent[0] and food_poss_y == agent[1]):
                    break

        food = [food_poss_x, food_poss_y]
        return agent, food

    def edit_block(this, x, y, value): this.maze[x][y] = value

    def update_maze(self, agent_pos, x, y):
        self.edit_block(agent_pos[0], agent_pos[1], SPACE)
        self.edit_block(x, y, AGENT)

    def printMaze(this):
        for row in this.maze:
            for col in row:
                print(col, end="")
            print()

    def is_food(this, x, y): return this.maze[x][y] == FOOD

    def is_space(this, x, y): return this.maze[x][y] == SPACE

    maze = readMaze("env3.txt")
