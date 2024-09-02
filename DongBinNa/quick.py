array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start,end) :
    if start >= end : # 원소가 1개인 경우 종료
        return
    pivot = start # pivot을 첫번째 원소로
    left = start + 1 #피벗 바로 다음 첫번째 원소로
    right = end # 끝에서 부터 반대로 탐색
    while left <= right :
        # 피벗보다 큰 데이터를 찾을 때까지 탐색
        while left <= end and array[left] <= array[pivot] :
            left += 1
        # 피벗보다 작은 데이터 찾을 때까지 탐색
        while right > start and array[right] >= array[pivot] :
            right -= 1
        # 피벗보다 큰데이터(오른쪽에서) 작은데이터(왼쪽에서) 엇갈린다면 교체
        if left > right :
            array[right], array[pivot] = array[pivot], array[right]
        # 안엇갈린다면 작은 데이터와 큰데이터만 교체
        else :
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 편과 오른쪽 편 나눠서 다시 진행 원소가 1개남을때까지
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)

## 쉬운버전

arrayEasy = [5,7,9,0,3,1,6,2,4,8]

def quick_sort_E(array) :
    ## 리스트가 하나 이하의 원소담으면 종료
    if len(array) <= 1 : return array

    pivot = array[0] # 피벗은 첫원소
    tail = array[1:] # 피벗 제외

    left_side = [x for x in tail if x<=pivot] # 분할 왼쪽 부분
    right_side = [x for x in tail if x>pivot] # 분할 오른쪽 부분

    # 분할 이후 왼족 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
    return quick_sort_E(left_side) + [pivot] + quick_sort_E(right_side)

print(quick_sort_E(arrayEasy))
