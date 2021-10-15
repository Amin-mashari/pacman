from maze import *
from Position import choosePosition

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
agent_memory = [[agent_pos[0], agent_pos[1], False, 1], ]


def environment(action):
    pass
# return percept
# percept = ["x_pos" , "y_pos" , "is_food"]


def agent(percept):
    pass
# return action


def main():
    print(choosePosition(agent_memory[0]))


if(__name__ == "__main__"):
    main()
