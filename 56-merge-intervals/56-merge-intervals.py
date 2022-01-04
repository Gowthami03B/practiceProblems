class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # //sorting
        intervals.sort(key = lambda x : x[0])
        merged = []
        for interval in intervals:
            # if merged is empty or second list's first element is greater than last list's last element, then just add
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # else select the max between last intervals last element, current intervals last element and
            # modify it as last intervals last
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged