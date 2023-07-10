from collections import deque

N, M = map(int, input().split())
maze = []
for _ in range(N) :
    maze.append(list(map(int,input())))



def bfs(n, m,maze):
    #queue를 사용
    queue = deque()
    queue.append((0,0)) # 시작 위치
    visited = [[False] * m for _ in range(n)]  # 방문 여부를 저장하는 배열
    visited[0][0] = True  # 시작 위치 방문 처리

    # 상하좌우 이동
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue :
        #for문 돌았는데
        y, x = queue.popleft()
        if x == m-1 and y == n-1:
            return maze[y][x] #도착했을때의 이동한 칸 개수

        for i in range(4) : #상하좌우를 살펴봄
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0 and maze[ny][nx] == 1:
                visited[ny][nx] = True
                maze[ny][nx] = maze[y][x] + 1 # 이동한 칸 개수 저장
                queue.append((ny, nx))
    return -1  # 탈출 실패

print(bfs(N,M,maze))