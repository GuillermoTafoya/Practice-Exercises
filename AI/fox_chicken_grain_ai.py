# Min max algorithm
# [Robot, Fox, Chicken, Grain]

import itertools as it

class tree:
    def __init__(self, value, state, depth):
        self.value = value
        self.state = state
        self.sons = []
        self.depth = depth

def solve(maxPassengers, maxDepth): # Up to how many passengers can you carry
    currentState = [True, True, True, True] # initial state
    targetState = [False, False, False, False]
    gameTree = tree(validityCheck(currentState, targetState), currentState, 0)

    bestTree = generateGameTree(gameTree,currentState,targetState, maxPassengers, 1, dict(),maxDepth)
    return bestTree

def move(currentState, targetState, combination, guessOfPassengers, depth, memo, gameTree):
    state = currentState.copy()
    
    for i in combination[:guessOfPassengers]:
        if state[i] == state[0]: # They can only move if they are on the same side as the robot
            state[i] = not state[i]

    state[0] = not state[0]

    constCurrentState = const(state)

    if constCurrentState in memo.keys() and validityCheck(state, targetState) != 1:
        return
    elif constCurrentState in memo.keys() and memo[constCurrentState] is not None and depth > memo[constCurrentState].depth:
        return

    value = validityCheck(state, targetState)

    gameTree.sons.append(tree(value, state, depth))
    memo[constCurrentState] = None

def generateGameTree(gameTree, currentState, targetState, maxPassengers, depth, memo, maxDepth):
    if depth > maxDepth or gameTree.value == 1:
        return
    constCurrentState = const(currentState)
    if constCurrentState in memo.keys() and memo[constCurrentState] != None and depth > memo[constCurrentState].depth:
        return

    currentMaxPassengers = min(maxPassengers, onTheSameSide(currentState))

    for guessOfPassengers in range(currentMaxPassengers+1):
        possiblePassengers = getCombinations({1,2,3}, guessOfPassengers)
        for combination in possiblePassengers: # Possible combinations
            move(currentState, targetState, combination, guessOfPassengers, depth, memo, gameTree)
        for son in gameTree.sons:
            if son.value == 0:
                generateGameTree(son, son.state, targetState, maxPassengers, depth+1, memo, maxDepth)

    gameTree.value = maxSonValue(gameTree)
    gameTree.depth = getDepthOfTree(gameTree)
    memo[constCurrentState] = gameTree
    return memo[constCurrentState]

def getDepthOfTree(gameTree):
    depth = float("inf")
    for son in gameTree.sons:
        if son.value > -1 and son.depth < depth:
            depth = son.depth
    return depth

def validityCheck(state,targetState):
    if state[1] == state[2] and state[1] != state[0]:
        # The fox ate the chicken
        return -1
    if state[2] == state[3] and state[2] != state[0]:
        # The chicken ate the grain
        return -1
    if state == targetState:
        # The problem is solved
        return 1
    return 0

def onTheSameSide(currentState):
    # How many are on the same side as the bot
    robot = currentState[0]
    counter = 0
    for i in range(1,len(currentState)):
        if currentState[i] == robot:
            counter += 1
    return counter

def maxSonValue(gameTree):
    currentMax = -2
    for son in gameTree.sons:
        if son.value > currentMax:
            currentMax = son.value
        if currentMax == 1:
            break
    return currentMax

def getCombinations(set, passengers):
    return list(it.combinations(set, r=passengers))

def const(array):
    return str(array)

def showSolution(bestTree)->list:
    """ Return an array with the best state achieved and the minimum trips 
        necessary if the problem is solvable"""
    bestSon = bestTree
    solved = bestTree.value
    minDepth = bestTree.depth
    solution = []
    while bestSon.sons:
        #print(bestSon.state)
        solution.append(bestSon.state)
        bestSon = getBestSon(bestSon, minDepth)
    #print(bestSon.state)
    solution.append(bestSon.state)
    if solved == 1:
        #print("Minimum necessary total trips:", bestSon.depth)
        solution.append(minDepth)
    else:
        solution.append(-1)
    return solution


def getBestSon(bestSon, minDepth):
    bestValue = bestSon.value 
    for son in bestSon.sons:
        if son.value == bestValue and son.depth == minDepth:
            return son

def ai(maxPassengers = 2, maxTrips = 7):
    bestTree = solve(maxPassengers, maxTrips)
    solution = showSolution(bestTree)
    return solution



def main():
    maxPassengers= 1
    maxDepth = 7
    bestTree = solve(maxPassengers, maxDepth)

    if bestTree.value > 0:
        print("It is possible to solve the problem with", maxPassengers, "passengers and", maxDepth,"trips.")
    else:
        print("It is NOT possible to solve the problem with", maxPassengers, "passengers and", maxDepth,"trips.")
    showSolution(bestTree)

if __name__ == '__main__':
    main()