from collections import deque

n,m = map(int,input().split())

cheeze = []

for _ in range(n) :
    cheeze.append(list(map(int,input())))


visited = []
visited = [[False] * m for _ in range(n)]
visited [0][0] = 1;
