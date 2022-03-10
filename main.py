from Position import getRowPositionInMemory, choosePositionToGo
from maze import MAZE
import time
import copy

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
#global vars
NOT_SEEN_FOOD = True


def init_vars():
    global _agent_pos, _food_pos, _percept, agent_memory
    # get agent poss by read File


def get_possiton_index_in_memory(x, y):
    poss_row = getRowPositionInMemory(x, y, agent_memory)

    # row dosnt exist
    if(poss_row == -1):
        agent_memory.append([x, y, False, 1])
        poss_row = len(agent_memory)-1
    else:
        # add seen position times
        agent_memory[poss_row][3] += 1

    return poss_row


def set_agent_poss(a, b):
    _agent_pos[0] = a
    _agent_pos[1] = b


def agent_go_to_new_poss(action):
    x = _agent_pos[0]
    y = _agent_pos[1]

    match action:
        case "LEFT":
            y = y - 1
        case "RIGHT":
            y = y + 1
        case "UP":
            x = x - 1
        case "DOWN":
            x = x + 1

    _maze.update_agent_location(_agent_pos, x, y)
    set_agent_poss(x, y)


def is_same_poss(aPoss, fPoss):
    return aPoss[0] == fPoss[0] and aPoss[1] == fPoss[1]


def is_agent_find_food():
    return is_same_poss(_agent_pos, _food_pos)


def environment(action):
    agent_go_to_new_poss(action)

    if(is_agent_find_food()):
        global NOT_SEEN_FOOD
        NOT_SEEN_FOOD = False
        return

    x_cuurent = _agent_pos[0]
    y_cuurent = _agent_pos[1]

    poss_index_in_memory = get_possiton_index_in_memory(x_cuurent, y_cuurent)

    return agent_memory[poss_index_in_memory]

# return percept
# percept = ["x_pos" , "y_pos" , "is_food"]


def action(current_poss, choosen_poss):
    if(current_poss[0] < choosen_poss[0]):
        return "DOWN"

    elif(current_poss[0] > choosen_poss[0]):
        return "UP"
    else:
        if(current_poss[1] < choosen_poss[1]):
            return "RIGHT"
        else:
            return "LEFT"


def agent(percept):

    current_poss = [percept[0], percept[1]]
    choosen_poss = choosePositionToGo(percept, agent_memory, _maze)
    return action(current_poss, choosen_poss)
# return action


def main():

    percept = _percept
    agent_moves = 1
    first_agent_pos = copy.copy(_agent_pos)

    while(NOT_SEEN_FOOD):
        _maze.printMaze()
        print()
        agent_moves += 1
        percept = environment(agent(percept))
        time.sleep(0.5)

    _maze.printMaze()
    print()
    print("food has found! ")
    print(f'agent Moves: {agent_moves}')
    print(
        f'agent position was x:{first_agent_pos[0]} y:{first_agent_pos[1]+1}')
    print(f'food position is x:{_food_pos[0]} y:{_food_pos[1]+1}')

# start
_maze = MAZE("rand.txt")
_agent_pos, _food_pos = _maze.get_agent_and_food_poss_from_file()
# save agent curretn state and food status and seent time
#                x          y        foodstatus    seentimes
agent_memory = [[_agent_pos[0], _agent_pos[1], False, 1]]
_percept = agent_memory[0]

main()
