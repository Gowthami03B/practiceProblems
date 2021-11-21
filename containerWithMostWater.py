def maxArea(arr) : 
    start = 0
    end = len(arr) - 1
    area = 0
    while start < end:
        area = max(area, min(arr[start], arr[end]) * (end - start)) 
        if arr[start] < arr[end]:
            start+= 1
        else:
            end-= 1
        end
    end
    return area

arr = [3,1,2,4,5]
print(maxArea(arr))
