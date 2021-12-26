def avgSubArray(arr, k):
        if len(arr) < k:
            return []
        n = len(arr)
        final = []
        left = right = sum = 0
        for i in range(k):
            sum+= arr[i]
        final.append(sum)
        for i in range(1,n-k+1):
            sum = sum - arr[i-1] + arr[k]
            final.append(sum)
        final = [i / 5 for i in final]
        return final
arr =  [1, 3, 2, 6, -1, 4, 1, 8, 2]
print(avgSubArray(arr, 5))
