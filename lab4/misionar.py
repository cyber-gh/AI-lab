from copy import deepcopy as dp
from pprint import pprint as pp

M = 2


class State:
    def __init__(self, mal, config):
        self.mal = mal
        self.config = config

    def successors(self):
        ((bad_left, good_left), (bad_right, good_right)) = self.config

        return []

    def __eq__(self, other):
        return self.config == other.config and self.mal == other.mal

    def __ne__(self, other):
        return self.config != other.config and self.mal != other.mal

    def __repr__(self):
        return str(self.config)


class PathState:
    def __init__(self, state, cost, parent_state):
        self.parent_state = parent_state
        self.state = state
        self.cost = cost

    def heuristic(self, target_state):
        return 0

    def __repr__(self):
        return str(self.state.config) + ", " + str(self.cost)


visited = []

if __name__ == '__main__':
    start_state = State(0, ((3, 3), (0, 0)))
    target_state = State(1, ((0, 0), (3, 3)))

    open_list = [PathState(dp(start_state), 0, None)]
    visited = [PathState(dp(start_state), 0, None)]

    while len(open_list) > 0:
        open_list.sort(key=lambda pth: pth.cost + pth.heuristic(target_state))
        current = open_list.pop(0)
        if current.state == target_state:
            print("success " + str(current.cost))
            it = current
            while True:
                print(it.state)
                if it.parent_state is None:
                    break
                it = it.parent_state
            break
        for nxt in current.state.successors():
            new_cost = current.cost + 1
            old_path_state = next((node for node in visited if node.state == nxt), None)

            if old_path_state is None:
                open_list.append(PathState(nxt, new_cost, current))
                visited.append(PathState(nxt, new_cost, current))
            else:
                if new_cost < old_path_state.cost:
                    open_list = open_list.filter(lambda x: x.state != old_path_state.state)
                    visited = visited.filter(lambda x: x.state != old_path_state.state)
                    open_list.append(PathState(nxt, new_cost, current))
                    visited.append(PathState(nxt, new_cost, current))
