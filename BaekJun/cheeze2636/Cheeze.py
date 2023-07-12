from collections import deque

n, m = map(int,input().split())

cheeze = []
for _ in range(n):
    cheeze.append(list(map(int, input().split())))

visited = []


count = []

def bfs() :
    queue = deque()
    queue.append([0,0])
    visited = [[False] * m for _ in range(n)]
    visited [0][0] = 1;
    cnt = 0; #남은 치즈 개수
    while queue :
        x, y = queue.popleft()
        #상하좌우
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
                if cheeze[nx][ny] == 0 : # 주위에 치즈 있는지 확인
                    visited[nx][ny] =1
                    queue.append([nx,ny])
                elif cheeze[nx][ny] == 1 : #치즈 있으면 앞에 살피면 안됨 그래서 queue에 넣지않음
                    #대신 다음을 위해 치즈를 녹여줌
                    cheeze[nx][ny] = 0
                    visited[nx][ny] = 1
                    cnt+=1

    #마지막까지 바깥공기를 확인하고 나면 반환
    count.append(cnt)
    return cnt

#반복 횟수
time = 0
while True :
    #치즈가 다 증발할때 까지
    leftCheeze = bfs()
    #치즈가 0개로 반환 되었을때
    if leftCheeze == 0 :
        print(time)
        #몇번 돌아서 들어갔는 지 모르니 마지막은 -1 마지막에서 두번째에 남은 치즈를 구해야하니 -2
        print(count[-2])
        break
    time += 1









