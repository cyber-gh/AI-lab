estimates = {
    "a": 0,
    "b": 10,
    "f": 0,
    "e": 8,
    "c": 3,
    "g": 14,
    "d": 7,
    "i": 3,
    "k": 2,
    "j": 1
}
neighbours = {
    "a": [("b", 3), ("c", 9), ("d", 7)],
    "b": [("f", 100), ("e", 4)],
    "c": [("e", 10), ("g", 6)],
    "d": [("i", 4)],
    "e": [("c", 1), ("f", 8)],
    "f": [],
    "g": [("e", 7)],
    "i": [("j", 2), ("k", 1)],
    "j": [],
    "k": []
}

visited = dict()
parent = dict()
g = dict()

start_node = "a"
end_node = "f"


class PathNode:

    def __init__(self, node, cost):
        self.cost = cost
        self.node = node
        self.aproximation = estimates[node]


if __name__ == "__main__":
    open_list = [PathNode("a", 0)]
    parent["a"] = "x"

    while len(open_list) > 0:
        open_list.sort(key=lambda node: node.aproximation + node.cost, reverse=False)
        current = open_list[0]
        open_list.pop(0)
        if current.node == end_node:
            print("total cost = ", current.cost)
            print("path = ")

            it = current.node
            while True:
                print(it)
                if not (it in parent):
                    break
                it = parent[it]

            break
        for nxt, weight in neighbours[current.node]:
            new_cost = current.cost + weight

            old_path_node = next((node for node in open_list if node.node == nxt), None)
            if old_path_node is not None:
                if new_cost < old_path_node.cost:
                    old_path_node.cost = new_cost
                    parent[old_path_node.node] = current.node
                    g[old_path_node.node] = new_cost
                    open_list = [x for x in open_list if x.node != old_path_node.node]
                    open_list.append(old_path_node)
            else:
                if not (nxt in g):
                    open_list.append(PathNode(nxt, new_cost))
                    parent[nxt] = current.node
                    g[nxt] = new_cost
                else:
                    if new_cost < g[nxt]:
                        g[nxt] = new_cost
                        parent[nxt] = current.node
                        open_list.append(PathNode(nxt, new_cost))
