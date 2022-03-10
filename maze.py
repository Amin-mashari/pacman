from random import randrange, shuffle
import math

AGENT = "a"
FOOD = "f"
WALL = "*"
SPACE = "-"
maze_folder = "envirements//"


class MAZE:

    def __init__(self, filename):
        try:
            self.maze = self.read_maze_from_file(filename)
        except:
            self.save_maze_in_file(filename)
            self.maze = self.read_maze_from_file(filename)

    __agentPos = [-1, -1]
    __foodPos = [-1, -1]

    def getAgentPosition(self):
        return self.__agentPos

    def get_agent_and_food_poss_from_file(self):
        return self.__agentPos, self.__foodPos

    def getAgentPossRandomly(self):
        while True:
            agent_poss_x = randrange(1, len(self.maze) - 1)
            agent_poss_y = randrange(1, len(self.maze[agent_poss_x]) - 1)

            if(self.maze[agent_poss_x][agent_poss_y] == SPACE):
                break

        return [agent_poss_x, agent_poss_y]

    def getAgentAndFoodPossRandomly(self):
        agent = self.getAgentPossRandomly()

        while True:
            food_poss_x = randrange(1, len(self.maze) - 1)
            food_poss_y = randrange(1, len(self.maze[food_poss_x]) - 1)

            if(self.maze[food_poss_x][food_poss_y] == SPACE):
                if not(food_poss_x == agent[0] and food_poss_y == agent[1]):
                    break

        food = [food_poss_x, food_poss_y]
        return [agent, food]

    def edit_block(self, x, y, value): self.maze[x][y] = value

    def update_agent_location(self, agent_pos, x, y):
        self.edit_block(agent_pos[0], agent_pos[1], SPACE)
        self.edit_block(x, y, AGENT)

    def printMaze(self):
        for row in self.maze:
            for col in row:
                print(col, end="")
            print()

    def is_food(self, x, y): return self.maze[x][y] == FOOD

    def is_space(self, x, y): return self.maze[x][y] == SPACE

    def agent_not_found(self):
        return self.__agentPos[0] == -1 or self.__foodPos[0] == -1

    def generate_random_position_for_agent_and_food(self):
        self.__agentPos, self.__foodPos = self.getAgentAndFoodPossRandomly()

    def read_maze_from_file(self, filename):
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
                    self.__agentPos[0] = x
                    self.__agentPos[1] = y

                elif(i == FOOD):
                    self.__foodPos[0] = x
                    self.__foodPos[1] = y
                y += 1
            x += 1
        self.maze = maze
        if(self.agent_not_found()):
            self.generate_random_position_for_agent_and_food()
            self.update_maze()
        return maze

    def update_maze(self):
        self.edit_block(self.__agentPos[0], self.__agentPos[1], AGENT)
        self.edit_block(self.__foodPos[0], self.__foodPos[1], FOOD)

    def checkNumbersAreStandardFodMaze(self,_w, _h):
        if(_w < 5):
            _w = 5
        if(_h < 5):
            _h = 5
        return _w, _h

    def generate_maze(self, r=5, c=5):
        r, c = self.checkNumbersAreStandardFodMaze(r, c)
        col = math.ceil(r/2) - 1
        row = math.ceil(c/2) - 1
        vis = [[0] * row + [1] for _ in range(col)] + [[1] * (row + 1)]
        ver = [["*-"] * row + ['*'] for _ in range(col)] + [[]]
        hor = [["**"] * row + ['*'] for _ in range(col + 1)]

        # vis = [[0] * col + [1] for _ in range(row)] + [[1] * (col + 1)]
        # ver = [["*-"] * col + ['*'] for _ in range(row)] + [[]]
        # hor = [["**"] * col + ['*'] for _ in range(row + 1)]

        def walk(x, y):
            vis[y][x] = 1

            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]:
                    continue
                if xx == x:
                    hor[max(y, yy)][x] = "*-"
                if yy == y:
                    ver[y][max(x, xx)] = "--"
                walk(xx, yy)

        walk(randrange(col), randrange(row))

        s = f'{r},{c}\n'
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s

    def save_maze_in_file(self, filename):
        r, c = input("insert m , n: ").split()
        row = int(r)
        column = int(c)
        maze = self.generate_maze(row, column)
        text_file = open((maze_folder + filename), "w")
        text_file.write(maze)
        text_file.close()
