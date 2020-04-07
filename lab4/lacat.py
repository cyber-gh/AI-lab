from copy import deepcopy as dp
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
    def __init__(self, state, cost, parent_state):
        self.parent_state = parent_state
        self.state = state
        self.cost = cost

    def heuristic(self, target_state):

        return sum(abs(x) for x in self.state.config)

    def __repr__(self):
        return str(self.state) + ", " + str(self.cost)


visited = []
memorized = dict()

def readKeys():
    lst = []
    with open("lacat.txt","r") as fin:
        for line in fin.readlines():
            lst.append(line[:-1])
    return lst

if __name__ == '__main__':

    keys = readKeys()

    print(keys)

    start_state = State([1] * 7, keys)
    target_state = State([0] * 7, keys)

    open_list = [PathState(dp(start_state), 0, None)]
    visited = [PathState(dp(start_state), 0, None)]
    memorized[start_state] = PathState(dp(start_state), 0, None)

    while len(open_list) > 0:
        open_list.sort(key=lambda pth: pth.cost + pth.heuristic(target_state))
        current = open_list.pop(0)

        if current.state == target_state:
            it = current
            counter = 0
            while True:
                counter += 1
                print(it.state)
                if it.parent_state is None:
                    break
                it = it.parent_state
            print(counter)
            break
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
