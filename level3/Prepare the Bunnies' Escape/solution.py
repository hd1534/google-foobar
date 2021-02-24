length = 0

def dfs(arr, x, y, dep):

    if arr[x][y] == -1:
        return
    if arr[x][y] <= dep:
        return
    arr[x][y] = dep

    for x_move, y_move in [(1,0), (-1,0), (0,1), (0,-1)]:
        dfs(arr, x + x_move, y + y_move, dep + 1)


def solution(_map):
    length = len(_map)
    door_to_pod = [[-1 for _ in range(length + 2)] for _ in range(length + 2)]
    pod_to_door = [[-1 for _ in range(length + 2)] for _ in range(length + 2)]

    for i in range(length):
        for j in range(length):
            if _map[i][j] == 1:
                door_to_pod[i+1][j+1] = -1
                pod_to_door[i+1][j+1] = -1
            else:
                door_to_pod[i+1][j+1] = 999999999999999
                pod_to_door[i+1][j+1] = 999999999999999

    
    dfs(door_to_pod, 1, 1, 1)
    dfs(pod_to_door, length, length, 1)
    result = door_to_pod[length][length]

    # print("door to pod")
    # for i in door_to_pod:
    #     print(i)
    # print("\npod to door")
    # for i in pod_to_door:
    #     print(i)

    for i in range(1, length + 1):
        for j in range(1, length + 1):
            if pod_to_door[i][j] == -1:
                if pod_to_door[i-1][j] != -1 and pod_to_door[i+1][j] != -1:
                    result = min(result, pod_to_door[i-1][j] + door_to_pod[i+1][j] + 1, pod_to_door[i+1][j] + door_to_pod[i-1][j] + 1)
                if pod_to_door[i][j-1] != -1 and pod_to_door[i][j+1] != -1:
                    result = min(result, pod_to_door[i][j-1] + door_to_pod[i][j+1] + 1, pod_to_door[i][j+1] + door_to_pod[i][j-1] + 1)

    return result


print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))