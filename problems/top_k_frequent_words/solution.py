class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        window = {}
        for s in words:
            if(s in window):
                window[s] += 1
            else:
                window[s] = 1
        sorted_dick = sorted(window.items(), key=lambda x: (-x[1], x[0]))
        print(sorted_dick)
        return [i[0] for i in sorted_dick][:k]
            