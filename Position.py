from random import randrange


def is_same(a, b): return a == b


def is_same_position(x1, y1, possAray):
    x = possAray[0]
    y = possAray[1]
    return is_same(x1, x) and is_same(y1, y)


def get_position_row_in_memory(x, y, agent_memory):

    for i in range(len(agent_memory)):
        if(is_same_position(x, y, agent_memory[i])):
            return i
    return -1


def get_avail_pathes(current_x, current_y , maze):
    avil_positions = []
    
    # right
    if(maze.is_food(current_x + 1, current_y) or maze.is_space(current_x + 1, current_y)):
        avil_positions.append([current_x+1, current_y])
    # left
    if(maze.is_food(current_x - 1, current_y) or maze.is_space(current_x - 1, current_y)):
        avil_positions.append([current_x-1, current_y])
    # up
    if(maze.is_food(current_x, current_y + 1) or maze.is_space(current_x, current_y + 1)):
        avil_positions.append([current_x, current_y+1])
    # down
    if(maze.is_food(current_x, current_y - 1) or maze.is_space(current_x, current_y - 1)):
        avil_positions.append([current_x, current_y-1])

    return avil_positions


def is_poss_seen(poss, agent_memory):
    for percept in agent_memory:
        if(percept[0] == poss[0] and percept[1] == poss[1]):
            return True
    return False


def get_seen_poss_time(poss, agent_memory):
    for percept in agent_memory:
        if(percept[0] == poss[0] and percept[1] == poss[1]):
            return percept[3]
    return 0


def get_min_seen_poss(pathes, agent_memory):
    min = 10000
    choisen_poss = []
    for poss in pathes:
        temp = get_seen_poss_time(poss, agent_memory)
        if(temp < min):
            min = temp
            choisen_poss = poss

    return choisen_poss


def look_around_for_food_location(avail_pathes,maze):
    for x in avail_pathes:
        if(maze.is_food(x[0], x[1])):
            return x[0], x[1]
    return -1, -1


def is_food_finded(food_poss):
    if(food_poss[0] == -1):
        return False
    return True

# return x , y


def choose_poss_to_go(percept, agent_memory , maze):
    x_pos = percept[0]
    y_pos = percept[1]
    avail_pathes = get_avail_pathes(x_pos, y_pos,maze)

    # check food is around
    food_poss = look_around_for_food_location(avail_pathes,maze)
    if(is_food_finded(food_poss)):
        return food_poss

    # else
    not_seen_poss = []

    for poss in avail_pathes:
        if not(is_poss_seen(poss, agent_memory)):
            not_seen_poss.append(poss)

    if not(not_seen_poss):
        return get_min_seen_poss(avail_pathes, agent_memory)
    else:
        rand = randrange(len(not_seen_poss))
        return not_seen_poss[rand]
