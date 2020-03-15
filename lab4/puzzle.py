from copy import deepcopy as dp
from pprint import pprint as pp


class State:
    def __init__(self, config, x, y):
        self.y = y
        self.x = x
        self.config = config
        self.n = len(config)

    def successors(self):
        dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        for dx, dy in dxy:
            nxt_x = self.x + dx
            nxt_y = self.y + dy
            if 0 <= nxt_x < self.n and 0 <= nxt_y < self.n:
                cpy = dp(self.config)
                cpy[nxt_x][nxt_y], cpy[self.x][self.y] = cpy[self.x][self.y], cpy[nxt_x][nxt_y]
                yield State(cpy, nxt_x, nxt_y)

    def __hash__(self):
        return hash(tuple(tuple(x) for x in self.config))

    def __eq__(self, other):
        return self.config == other.config

    def __ne__(self, other):
        return self.config != other.config

    def __repr__(self):
        return str(self.config) + "x = {}, y = {}".format(self.x, self.y)

    def __str__(self):
        return str(self.config) + "x = {}, y = {}".format(self.x, self.y)


class PathState:
    def __init__(self, state, cost, parent_state):
        self.parent_state = parent_state
        self.state = state
        self.cost = cost

    def heuristic(self, target_state):
        tg = target_state.config
        st = self.state.config
        tst = { tg[i][j]: (i, j) for i in range(0, len(tg)) for j in range(0, len(tg))}
        cnt = 0
        for idx in range(0, len(tg)):
            for i in range(0, len(tg)):
                cnt += abs(idx - tst[st[idx][i]][0]) + abs(i - tst[st[idx][i]][1])

        return cnt

    def __repr__(self):
        return str(self.state) + ", " + str(self.cost)


visited = []
memorized = dict()

if __name__ == '__main__':
    start_state = State([[1, 2, 3], [4, 5, 8], [6, 7, 0]], 2, 2)
    target_state = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]], 2, 2)

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
