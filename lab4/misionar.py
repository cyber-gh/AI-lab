from copy import deepcopy as dp
from pprint import pprint as pp


class State:
    def __init__(self, missionary_left, cannibals_left, missionary_right, cannibals_right, boat_capacity, boat_beach):
        self.boat_beach = boat_beach
        self.boat_capacity = boat_capacity
        self.cannibals_right = cannibals_right
        self.missionary_right = missionary_right
        self.cannibals_left = cannibals_left
        self.missionary_left = missionary_left

    def get_tuple(self):
        return self.cannibals_left, self.cannibals_right, self.missionary_left, self.missionary_right, self.boat_beach

    def is_good(self):
        if 1 <= self.missionary_left < self.cannibals_left:
            return False
        if 1 <= self.missionary_right < self.cannibals_right:
            return False
        return True

    def successors(self):
        st = dp(self)

        if st.boat_beach == 0:
            for can in range(0, st.cannibals_left + 1):
                for miss in range(0, st.missionary_left + 1):
                    if 0 < can + miss <= st.boat_capacity and \
                            ((miss >= can) or (miss == 0)):
                        next_state = dp(st)
                        next_state.cannibals_left -= can
                        next_state.missionary_left -= miss
                        next_state.cannibals_right += can
                        next_state.missionary_right += miss
                        next_state.boat_beach = 1 - st.boat_beach
                        if next_state.is_good():
                            yield next_state
        else:
            for can in range(0, st.cannibals_right + 1):
                for miss in range(0, st.missionary_right + 1):
                    if 0 < can + miss <= st.boat_capacity and \
                            ((miss >= can) or (miss == 0)):
                        next_state = dp(st)
                        next_state.cannibals_right -= can
                        next_state.missionary_right -= miss
                        next_state.cannibals_left += can
                        next_state.missionary_left += miss
                        next_state.boat_beach = 1 - st.boat_beach
                        if next_state.is_good():
                            yield next_state

    def __hash__(self):
        return hash(self.get_tuple())

    def __eq__(self, other):
        return self.get_tuple() == other.get_tuple()

    def __ne__(self, other):
        return self.get_tuple() != other.get_tuple()

    def __str__(self):
        return "left {} : {}, right {} : {}, {}".format(self.cannibals_left, self.missionary_left, self.cannibals_right,
                                                  self.missionary_right, self.boat_beach)


class PathState:
    def __init__(self, state, cost, parent_state):
        self.parent_state = parent_state
        self.state = state
        self.cost = cost

    def heuristic(self):
        st = self.state
        return (st.cannibals_left + st.missionary_left) // st.boat_capacity

    def __repr__(self):
        return str(self.state) + ", " + str(self.cost)


visited = []
memorized = dict()

if __name__ == '__main__':
    M = 3
    N = 5
    start_state = State(N, N, 0, 0, M, 0)
    target_state = State(0, 0, N, N, M, 1)

    open_list = [PathState(dp(start_state), 0, None)]
    visited = [PathState(dp(start_state), 0, None)]
    memorized[start_state] = PathState(dp(start_state), 0, None)
    # for el in start_state.successors():
    #     print(el)
    #
    # tmp = State(3, 1, 0, 2, M, 1)
    # print(tmp.is_good())


    while len(open_list) > 0:
        open_list.sort(key=lambda pth: pth.cost + pth.heuristic())
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
