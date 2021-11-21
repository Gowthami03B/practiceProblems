def findInsertPos(arr, target) :
    start = 0
    end = len(arr) - 1
    while(start <= end):
        mid = (start+end)/2
        if(target == arr[mid]):
            return mid
        elif(target > arr[mid]):
            start = mid + 1
        else:
            end = mid - 1
    end
    return end + 1

arr = [1,5,89,100]
target = 5
print(findInsertPos(arr, target))
