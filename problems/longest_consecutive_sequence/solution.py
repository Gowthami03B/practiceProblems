class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set: #if num - 1 is not in set, then sequence starts here. if num - 1 in set, then num is already included in the sequence by num - 1
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
    def longestConsecutiveBruteForce(self, nums):
        longest = 0
        for num in nums:
            curr = num
            currStreak = 1
            while curr + 1 in nums:
                curr += 1
                currStreak += 1
            longest = max(longest, currStreak)
        return longest