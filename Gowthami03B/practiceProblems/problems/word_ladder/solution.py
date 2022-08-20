class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        L = len(beginWord)
        if endWord not in wordList or not endWord or not beginWord:
            return 0
        dict_comb = defaultdict(list)
        for word in wordList:
            for i in range(L):
                dict_comb[word[:i] + '*' + word[i+1:]].append(word)
        print(dict_comb)
        queue = collections.deque([(beginWord,1)])
        visited = set()
        visited.add(beginWord)
        while queue:
            curr_word,level=queue.popleft()
            for i in range(L):
                intermediate_word = curr_word[:i] + '*' +curr_word[i+1:]
                for word in dict_comb[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        queue.append((word,level+1))
                        visited.add(word)
                dict_comb[intermediate_word] = []     
        return 0
                        