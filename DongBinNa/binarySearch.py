def binarySearch(arr,target,start,end) :
    if start > end :
        return None
    mid = (start+end)//2
    if arr[mid] == target :
        return mid
    elif arr[mid] < target :
        return binarySearch(arr,target,mid+1,end)
    else :
        return binarySearch(arr,target,start,mid-1)

arr = [1,3,5,7,9,11,13,15,17,19,23]
target = 13

result = binarySearch(arr,target,0,len(arr)-1)

if result == None :
    print("찾는게 없네?")
else :
    print(result + 1, "번째ㅁ에 있습니다")