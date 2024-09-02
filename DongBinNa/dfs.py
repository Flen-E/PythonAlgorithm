N = 4
M = 5

array =[[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]

# 동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

visited = [(False)* M]*N
result = 0

def dfs(x,y) :

    if x <= -1 or x >= N or y <= -1 or y >= M :
        return False
    # 방문하지 않았더라면
    if array[x][y] == 0 :
        # 해당 노드는 1로 바꾸어 다음 방문식 false 반환
        array[x][y] = 1
        # 인접한 노드를 재귀하여 1로 바꾸어 false가 반환되어 result가 안늘게함
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False


for i in range(len(array)):
    for j in range(len(array[i])):
        if dfs(i, j) == True:
            result += 1

print(result)