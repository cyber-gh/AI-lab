from copy import deepcopy as dp
from pprint import pprint as pp


class State:
    def __init__(self, config):
        self.config = config

    def successors(self):
        state_cpy = dp(self.config)
        configs = []

        for i, lst in enumerate(state_cpy):
            if len(lst) == 0:
                continue

            new_config = dp(state_cpy)

            el = new_config[i].pop(0)

            for j, x in enumerate(new_config):
                if i == j:
                    continue

                succ = dp(new_config)
                succ[j].insert(0, el)

                configs.append(State(succ))

        return configs

    def __eq__(self, other):
        return self.config == other.config

    def __repr__(self):
        return str(self.config)


class PathState:
    def __init__(self, state, cost, parent_state):
        self.parent_state = parent_state
        self.state = state
        self.cost = cost

    def heuristic(self, target_state):
        tg = target_state.config
        st = self.state.config
        cnt = 0
        for idx in range(0, len(tg)):
            for i in range(0, min(len(st[idx]), len(tg[idx]))):
                if st[idx][i] != tg[idx][i]:
                    cnt += 1
            cnt += max(0, len(st[idx]) - len(tg[idx]))

        return cnt

    def __repr__(self):
        return str(self.state.config) + ", " + str(self.cost)


visited = []

if __name__ == '__main__':
    start_state = State([["a"], ["b", "c"], ["d"]])
    target_state = State([["c", "b"], [], ["a", "d"]])

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
