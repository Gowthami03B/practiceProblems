# Given a sorted array A ( sorted in ascending order ),
# find if there exists 2 integers A[i] and A[j] such that A[i] + A[j] = 0, i != j 

def findVal(nums):
    i ,j = 0, len(nums) - 1
    for i in range(len(nums)):
        while(j > i):
            if nums[i] + nums[j] == 0:
                return True
            if nums[i] + nums[j] < 0:
                break;
            j -= 1
    return False

nums = [-3,-2,-1,1,6,8,9,20]
print(findVal(nums))
#intuition - so when -3+20 > 0; we know that for all i+1 values, the sum would be > 0 hence we can decrement j
#and achieve O(N) solution
#naive solution is doing 2 loops and getting O(N2)
