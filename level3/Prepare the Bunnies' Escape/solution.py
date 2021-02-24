from collections import deque


def bfs(_map, x, y):
    height = len(_map[0])
    width = len(_map)

    arr = [[ None for _ in range(height)] for _ in range(width)]
    arr[x][y] = 1

    queue = deque([(x, y)])
    while queue:
        x, y = queue.pop()
        for x_move, y_move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_x, next_y = x + x_move, y + y_move
            
            if 0 <= next_x < width and 0 <= next_y < height and arr[next_x][next_y] is None:
                arr[next_x][next_y] = arr[x][y] + 1

                if _map[next_x][next_y] == 0:
                    queue.appendleft((next_x, next_y))

    return arr



def solution(_map):
    height = len(_map[0])
    width = len(_map)

    door_to_pod = bfs(_map, 0,0)
    pod_to_door = bfs(_map, width - 1, height - 1)

    # print("map")
    # for i in _map:
    #     print(i)
    # print("\ndoor to pod")
    # for i in door_to_pod:
    #     print(i)
    # print("\npod to door")
    # for i in pod_to_door:
    #     print(i)

    result = float('inf')
    for i in range(width):
        for j in range(height):
            if door_to_pod[i][j] and pod_to_door[i][j]:
                result = min(result, door_to_pod[i][j] + pod_to_door[i][j] - 1)

    return result
