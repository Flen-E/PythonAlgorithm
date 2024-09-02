array = [19,14,10,17]
M = 20
array.sort(reverse=True)

maxH = array[0]

for x in range(maxH,-1,-1):
    num = 0
    for i in range(len(array)-1) :
        if array[i] > x :
            num += array[i] - x
    if num == M :
        print(x)

## 현재 코딩은 n^2이 되기에 10억까지 정수라는 큰 범위를 보면 가장 먼저 이진 탐색을 떠올려야함

n, m = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0

# 이진탐색 수행
while(start <= end):
    total = 0
    mid = (start + end) //2
    for x in array :
        if x> mid:
            total += x -mid
    #양이 부족한 경우
    if total < m :
        end = mid -1
    else :
        result = mid
        start = mid + 1

print(result)