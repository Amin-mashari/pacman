from random import randrange, shuffle

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
            self.init_agent_and_food_position()
            self.save_agent_and_food_position_in_file()
            self.maze = self.read_maze_from_file(filename)

    __agentPos = [-1, -1]
    __foodPos = [-1, -1]

    def save_agent_and_food_position_in_file(self):
        pass

    def init_agent_and_food_position(self):
        if(self.__agentPos[0] == -1):
            self.__agentPos, self.__foodPos = self.getAgentAndFoodPossRandomly()

    def init_food_and_agent_poss_in_maze(self, agent_p, food_p):
        self.maze[agent_p[0]][agent_p[1]] = AGENT
        self.maze[food_p[0]][food_p[1]] = FOOD

    def get_agent_and_food_poss_from_file(self):
        if(self.__agentPos[0] == -1):
            agent_p, food_p = self.getAgentAndFoodPossRandomly()
            self.init_food_and_agent_poss_in_maze(agent_p, food_p)
            return agent_p, food_p
        else:
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

    def update_maze(self, agent_pos, x, y):
        self.edit_block(agent_pos[0], agent_pos[1], SPACE)
        self.edit_block(x, y, AGENT)

    def printMaze(self):
        for row in self.maze:
            for col in row:
                print(col, end="")
            print()

    def is_food(self, x, y): return self.maze[x][y] == FOOD

    def is_space(self, x, y): return self.maze[x][y] == SPACE

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
        return maze

    def generate_maze(self,w=16, h=8):
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

        s = f'{w},{h}\n'
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        return s

    def generate_agent_and_food_position(self,maze):
        print("AARR:\n")
        print(maze)
        print("AARR:\n")
        print(maze[0])
        print(len(maze))

    def save_maze_in_file(self, filename):
        r, c = input("insert m , n: ").split()
        row = int(r)
        column = int(c)
        maze = self.generate_maze(row, column)
        # maze = self.generate_agent_and_food_position(maze)
        self.generate_agent_and_food_position(maze)
        text_file = open((maze_folder + filename), "w")
        text_file.write(maze)
        text_file.close()
        
