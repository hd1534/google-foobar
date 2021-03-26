from collections import deque


class EdmondsKarp:
    "Solution using Edmonds-Karp Algorithm"

    def __init__(self, entrances, exits, path):
        self.entrances = entrances
        self.exits = exits
        self.path = path
        self.length = len(self.path)
        self.network = [
            [0 for _ in range(self.length+2)] for _ in range(self.length+2)]
        self.__setup_flow_network()

    def __setup_flow_network(self):
        """
        create flow network with 'one source' and 'one sink'
        : network[u][v] means c(u, v)
        """

        for source in self.entrances:
            self.network[0][source+1] = float('inf')

        for i in range(self.length):
            for j in range(self.length):
                self.network[i+1][j+1] = self.path[i][j]

        for sink in self.exits:
            self.network[sink+1][self.length+1] = float('inf')

        self.length += 2

    def find_path_bfs(self):
        "find 'source to sink' paths and return one of them"
        
        parents = [-1 for _ in range(len(self.network))]

        queue = deque()
        queue.append(0)
        while len(queue) > 0 and parents[-1] == -1:  #
            u = queue.popleft()
            for v, parent in enumerate(parents):
                if self.network[u][v] > 0 and parent == -1:
                    parents[v] = u  # parents[v] = u means c(u, v) > 0
                    queue.append(v)

        path = list()
        u = -1  # find 'sink to source' path
        while parents[u]:
            u = parents[u]

            if u == -1:
                return None  # no path to source
            path.append(u)
        path.reverse()

        return path

    def edmonds_karp(self):
        "return result using Edmonds Karp's algorithm"
        
        result = 0

        path = self.find_path_bfs()
        while path:
            capacity = float('inf')  # minnimum value of f(u, v)
            u = 0
            for v in path:
                capacity = min(capacity, self.network[u][v])
                u = v
            u = 0
            for v in path:
                self.network[u][v] -= capacity  # c(u, v) - f(u, v)
                # c(v, u) - f(v, u) = c(v, u) + f(u, v)
                self.network[v][u] += capacity
                u = v
            result += capacity

            path = self.find_path_bfs()

        return result


def solution(entrances, exits, path):
    # Your code here

    edmonds_karp = EdmondsKarp(entrances, exits, path)
    result = edmonds_karp.edmonds_karp()
    del edmonds_karp

    return result


if __name__ == '__main__':
    A = solution([0], [3], [[0, 7, 0, 0],
                            [0, 0, 6, 0],
                            [0, 0, 0, 8],
                            [9, 0, 0, 0]])
    print(A)

    B = solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0],
                                  [0, 0, 5, 2, 0, 0],
                                  [0, 0, 0, 0, 4, 4],
                                  [0, 0, 0, 0, 6, 6],
                                  [0, 0, 0, 0, 0, 0],
                                  [0, 0, 0, 0, 0, 0]])
    print(B)
