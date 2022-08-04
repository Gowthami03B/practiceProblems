class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        counts = defaultdict(int)
        start = 0
        for end in range(len(s)):
            counts[s[end]] += 1
            #So when the current length of the substring end-start+1 - max repeated chars > k; then we have exhausted our replacements and need to move forward hence subtract start value and start += 1
            while end - start + 1 - max(counts.values()) > k:
                counts[s[start]] -= 1
                start += 1
            result = max(result, end - start + 1)
            
        return result