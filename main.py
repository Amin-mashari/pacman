from Position import *


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
_agent_pos, _food_pos = getAgentAndFoodPossRandomly(maze)
agent_memory = [[_agent_pos[0], _agent_pos[1], False, 1]]
_percept = agent_memory[0]
NOT_SEEN_FOOD = True
_agent_path_to_food = []


def add_to_agent_memory(action):
    poss_index = get_poss(action[0], action[1], agent_memory)

    if(poss_index == -1):
        agent_memory.append([action[0], action[1], False, 1])
        poss_index = len(agent_memory)-1
    else:
        agent_memory[poss_index][3] += 1

    return poss_index

# action is poss


def environment(action):

    if(action[0] == _food_pos[0] and action[1] == _food_pos[1]):
        global NOT_SEEN_FOOD
        NOT_SEEN_FOOD = False
        return

    action_index = add_to_agent_memory(action)
    _agent_path_to_food.append([action[0], action[1]])

    return agent_memory[action_index]

# return percept
# percept = ["x_pos" , "y_pos" , "is_food"]


def agent(percept):
    return choosePosition(percept, agent_memory)
# return action


def main():
    percept = _percept
    
    while(NOT_SEEN_FOOD):
        percept = environment(agent(percept))
        
    print("path:")
    print(_agent_path_to_food)
    print("len:", len(_agent_path_to_food))
    #save_maze(25 , 30, "map5.txt")
    


if(__name__ == "__main__"):
    main()
