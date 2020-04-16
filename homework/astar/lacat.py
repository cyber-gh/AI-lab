from copy import deepcopy as dp
import time
from pprint import pprint as pp


class State:
    def __init__(self, config, keys):
        self.config = config
        self.keys = keys
        self.used_key = "no key"

    def successors(self):
        for key in keys:
            succ = dp(self)
            succ.used_key = key
            for index, el in enumerate(key):
                if el == "d":
                    succ.config[index] -= 1
                    succ.config[index] = max(succ.config[index], 0)
                if el == "i":
                    succ.config[index] += 1

            yield succ

    def __hash__(self):
        return hash(tuple(self.config))

    def __eq__(self, other):
        return self.config == other.config

    def __ne__(self, other):
        return self.config != other.config

    def __repr__(self):
        return str(self.config) + " " + self.used_key

    def __str__(self):
        return str(self.config) + " " + self.used_key


class PathState:

    HEURISITIC_TYPE = 1

    def __init__(self, state, cost, parent_state):
        self.parent_state = parent_state
        self.state = state
        self.cost = cost

    def heuristic(self, target_state):
        if PathState.HEURISITIC_TYPE == 1:
            return self.heuristic1(target_state)
        if PathState.HEURISITIC_TYPE == 2:
            return self.heuristic2(target_state)
        if PathState.HEURISITIC_TYPE == 3:
            return self.badHeuristic(target_state)

        raise ValueError("Unkown heuristic")

    def heuristic2(self, target_state):
        return max(x for x in self.state.config) - min(x for x in self.state.config)

    # def heuristic1(self, target_state):
    #     return sum(1 if x != 0 else 0 for x in self.state.config)

    def heuristic1(self, target_state):
        return max(x for x in self.state.config)

    def badHeuristic(self, target_state):
        return 2 * sum(x for x in self.state.config)

    def __repr__(self):
        return str(self.state) + ", " + str(self.cost)


visited = []
memorized = dict()

input_files = [
    "nosol.txt", # nu este solutie, nici o cheie nu descuie a doua usa
    "final.txt", # nu e posibil, trebuie sa fac cel putin o miscare
    "lacat2.txt", # solutia in 4 pasi
    "lacat.txt", # solutia in 8 pasi, badHeuristic rezolva in 9 pasi
]

def readKeys():
    lst = []
    with open(input_files[3], "r") as fin:
        for line in fin.readlines():
            lst.append(line[:-1])
    return lst


def showMeTheWay(way):
    way = way[::-1]

    for idx, stop in enumerate(way):
        if (idx != len(way) - 1):
            stop.used_key = way[idx + 1].used_key
    way[-1].used_key = "no key"


    print("initial state is \n" + str(way[0].config))
    for stop in way:
        print("on configuration {} apply the key {}".format(str(stop.config), stop.used_key))
    print("Reached target in {} steps".format(len(way)))



if __name__ == '__main__':
    foundSol = False
    start_time = time.time()
    keys = readKeys()

    print(keys)
    sz = len(keys[0])

    start_state = State([1] * sz, keys)
    target_state = State([0] * sz, keys)

    open_list = [PathState(dp(start_state), 0, None)]
    visited = [PathState(dp(start_state), 0, None)]
    memorized[start_state] = PathState(dp(start_state), 0, None)

    while len(open_list) > 0:
        open_list.sort(key=lambda pth: pth.cost + pth.heuristic(target_state))
        current = open_list.pop(0)

        if current.state == target_state:
            foundSol = True
            way = []
            it = current
            counter = 0
            while True:
                counter += 1
                way.append(it.state)
                if it.parent_state is None:
                    break
                it = it.parent_state
            showMeTheWay(way)
            break

        # if a door is locked and there is no key which unlocks that door there is no point in continuing
        locked = [idx for idx, x in enumerate(current.state.config) if x > 0]
        if any(sum(1 if key[idx] == 'd' else 0 for key in keys) == 0 for idx in locked):
            print("Skipping state {}".format(current.state))
            continue

        for nxt in current.state.successors():
            new_cost = current.cost + 1

            if not (nxt in memorized):
                open_list.append(PathState(nxt, new_cost, current))
                memorized[nxt] = PathState(nxt, new_cost, current)
            else:
                if new_cost < memorized[nxt].cost:
                    open_list = [x for x in open_list if x.state != memorized[nxt].state]
                    open_list.append(PathState(nxt, new_cost, current))
                    memorized[nxt].cost = new_cost
    if not foundSol:
        print("There is no solution")
    print("Time elapsed =  {} seconds".format(time.time() - start_time))
