class Solution:
    def minSteps(self, s: str, t: str) -> int:
        t_map = collections.defaultdict(int)
        for c in t:
            t_map[c] += 1
        for c in s:
            if c in t_map:
                if t_map[c] > 0:
                    t_map[c] -= 1

        return sum(t_map.values())

        