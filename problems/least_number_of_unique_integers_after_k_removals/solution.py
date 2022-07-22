class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count_map = defaultdict(int)
        for num in arr:
            count_map[num] += 1
        for num, count in sorted(count_map.items(), key= lambda x: x[1]):#loop through values in ascending order
            while k > 0 and count_map[num] > 0:
                count_map[num] -= 1
                k -= 1
            if count_map[num] == 0:#when 0 count, delete from map
                del count_map[num]
        return len(count_map)