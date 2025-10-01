arr = [
    [0, 1 ,1 ,1 ,1 ,1],
    [0, 1 ,0 ,0 ,0 ,1],
    [0, 1 ,0 ,1 ,0 ,1],
    [0, 1 ,0 ,1 ,0 ,0],
    [0, 0 ,0 ,1 ,1 ,0],
    [1, 1 ,1 ,1 ,1 ,0]
]

for i in range(len(arr)):   # width of arr
    print(arr[i])

print("-----------------------")


def maptoarr(row,column,list):
    arr = [[0]*column for _ in range(row)]
    data_index = 0

    for i in range(row):
        for j in range(column):
            arr[i][j] = list[data_index]
            data_index += 1

    return arr


list1 = [
    0, 1 ,1 ,1 ,1 ,1,
    0, 1 ,0 ,0 ,0 ,1,
    0, 1 ,0 ,1 ,0 ,1,
    0, 1 ,0 ,1 ,0 ,0,
    0, 0 ,0 ,1 ,1 ,0,
    1, 1 ,1 ,1 ,1 ,0
]

newarr = maptoarr(6,6,list1)
print(newarr)


R = len(newarr)
C = len(newarr[0])

# 위 아래 왼 오
DR = [-1,1,0,0]
DC = [0,0,-1,1]


def DFS(start_r,start_c):
    path = []
    stack = [(start_r,start_c)]
    visited = [[False]*C for _ in range(R)]
    visited[start_r][start_c] = True
    
    while stack:
        r,c = stack.pop()
        if r >= R or r < 0 or c >= C or c <0:
            continue
        path.append((r,c))
        for i in range(4):
            new_r = r +DR[i]
            new_c = c +DC[i]
            if new_r >= R or new_r < 0 or new_c >= C or new_c <0: # 생략
                continue
            if newarr[new_r][new_c] == 1:
                continue
            if not visited[new_r][new_c]:
                visited[new_r][new_c] = True
                stack.append((new_r,new_c))

    print('DFS - ',path)
    return path

DFS(0,0)

def BFS(start_r,start_c):
    path = []
    queue = [(start_r,start_c)]
    visited = [[False]*C for _ in range(R)]
    visited[start_r][start_c] = True

    while queue:
        r,c = queue.pop(0)
        if r >= R or r < 0 or c >= C or c <0:
            continue
        path.append((r,c))
        for i in range(4):
            new_r = r +DR[i]
            new_c = c +DC[i]
            if new_r >= R or new_r < 0 or new_c >= C or new_c <0:
                continue
            if newarr[new_r][new_c] == 1:
                continue
            if not visited[new_r][new_c]:
                visited[new_r][new_c] = True
                queue.append((new_r,new_c))

    print('BFS - ',path)
    return path


BFS(0,0)
