from collections import deque

n, m = map(int, input().split())

maze = []
for _ in range(n) :
    maze.append(list(map(int, input())))

def bfs() :
    #상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((0,0,1))
    visited[0][0][1] = 1;
    while queue:
        x, y, hited = queue.popleft()
        if (x == n - 1 and y == m - 1):
            return visited[x][y][hited]
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or nx >= n or ny < 0 or ny >= m :
                continue
            # 벽 부시지 않음
            if visited[nx][ny][hited] == 0 and maze[nx][ny] == 0:
                visited[nx][ny][hited] = visited[x][y][hited] + 1
                queue.append((nx, ny, hited))
            # 벽 뿌숨, 뿌술 능력이 있음
            if maze[nx][ny] == 1 and hited == 1:
                visited[nx][ny][hited - 1] = visited[x][y][hited] + 1
                queue.append((nx, ny, hited - 1))

    return -1

print(bfs())




