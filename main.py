from maze import *

"""
alghoritm
look around{
    move = getPath(x_agent , y_agent);
    all_moves{
        isSeen_all of them{
            choose min seen_pos
        }else{
            choose first pos you dont see
        }
    }
}
"""
maze = readMaze("map01.txt")
agent_pos, food_pos = getAgentPosition(maze)
agent_memory = [agent_pos[0], agent_pos[1], False]


def getPath(x, y):
    poss = []
    if(maze[x+1][y] == SPACE):
        poss.append(x+1, y)

    if(maze[x-1][y] == SPACE):
        poss.append(x-1, y)

    if(maze[x][y+1] == SPACE):
        poss.append(x, y+1)

    if(maze[x][y-1] == SPACE):
        poss.append(x, y-1)

    return poss


def choosePosition(percept):
    x_pos = percept[0]
    y_pos = percept[1]
    pathes = getPath(x_pos, y_pos)
    pass


def environment(action):
    pass
# return percept
# percept = ["x_pos" , "y_pos" , "is_food"]


def agent(percept):
    pass
# return action


def main():
    pass


if(__name__ == "__main__"):
    main()
