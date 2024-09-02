from collections import deque

N = 5
M = 6
array = [[1,0,1,0,1,0],[1,1,1,1,1,1],[0,0,0,0,0,1],[1,1,1,1,1,1],[1,1,1,1,1,1]]

# 동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(x,y) :
    queue = deque()
    queue.append((x,y))
    # queue가 빌때 까지 무한 반복
    while queue :
        x,y = queue.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M :
                continue
            if array[nx][ny] == 0 :
                continue
            if array[nx][ny] == 1 :
                array[nx][ny] = array[x][y] + 1
                queue.append((nx,ny))
    # queue가 없을때 : 모든 노드를 돌아봤을때
    return array[N - 1][M - 1]

print(bfs(0,0))