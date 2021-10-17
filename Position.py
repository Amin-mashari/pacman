from maze import *
from random import randrange


def get_poss(x, y, agent_memory):

    for i in range(len(agent_memory)):
        if(x == agent_memory[i][0] and y == agent_memory[i][1]):
            return i
    return -1


def getPath(x, y):
    poss = []
    # right
    if(maze[x+1][y] == SPACE):
        poss.append([x+1, y])
    # left
    if(maze[x-1][y] == SPACE):
        poss.append([x-1, y])
    # up
    if(maze[x][y+1] == SPACE):
        poss.append([x, y+1])
    # down
    if(maze[x][y-1] == SPACE):
        poss.append([x, y-1])

    return poss


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


def min_seen_poss(pathes, agent_memory):
    min = 10000
    choisen_poss = []
    for poss in pathes:
        temp = get_seen_poss_time(poss, agent_memory)
        if(temp < min):
            min = temp
            choisen_poss = poss

    return choisen_poss


def choosePosition(percept, agent_memory):
    x_pos = percept[0]
    y_pos = percept[1]
    pathes = getPath(x_pos, y_pos)
    not_seen_poss = []

    for poss in pathes:
        if not(is_poss_seen(poss, agent_memory)):
            not_seen_poss.append(poss)

    if not(not_seen_poss):
        return min_seen_poss(pathes, agent_memory)
    else:
        rand = randrange(len(not_seen_poss))
        return not_seen_poss[rand]
