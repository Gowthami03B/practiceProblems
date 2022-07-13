class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        #longest subarray would be prev len + 1 which is [i-1] and [j-1]
        #since starting with 1, you need to have +1 in array
        #similar to longest common subsequence
        dp = [[0 for _ in range(len(nums2) + 1)] for _ in range(len(nums1) + 1)]
        max_len = 0
        # for i in range(1,len(nums1) + 1):#since starting with 1, you need to have +1 in array
        #     for j in range(1,len(nums2) + 1):
        #         if nums1[i-1] == nums2[j-1]:#compare all values in nums1 with nums2
        #             dp[i][j] = dp[i-1][j-1] + 1
        #             max_len = max(max_len,dp[i][j])
        # print(dp)
        # return max_len
    
        for i in reversed(range(len(nums1))):
            for j in reversed(range(len(nums2))):
                if nums1[i] == nums2[j]:#compare all values in nums1 with nums2
                    dp[i][j] = dp[i+1][j+1] + 1
                    max_len = max(max_len,dp[i][j])
        return max_len
    
    