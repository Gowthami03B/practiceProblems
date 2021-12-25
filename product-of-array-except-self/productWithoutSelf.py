def productWithoutSelf(arr, ans):
        suffix = 1
        n = len(arr)
        ans.append(suffix)
        for i in range(1,n):
            ans.append(arr[i - 1] * ans[i - 1])
        for i in reversed(range(n)):
            ans[i] = ans[i] * suffix
            suffix *= arr[i]
        return ans
