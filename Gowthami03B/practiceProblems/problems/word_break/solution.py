class Solution:
    def wordBreak1(self, s: str, wordDict: List[str]) -> bool:
        word_set =set(wordDict)
        queue = deque()
        visited =set()
        queue.append(0)
        while queue:
            index = queue.popleft()
            if index in visited:
                continue
            for i in range(index+1, len(s) + 1):#search the word from index to i
                if s[index:i] in word_set:#if it's in word set, add to queue to search from next index
                    queue.append(i)
                    if i == len(s):#if we reach len(s) when word match happened, it means we visited the whole word
                        return True
            visited.add(index)
        return False#else False
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        queue = deque()
        queue.append(0)
        visited=set()
        while queue:
            index = queue.popleft()
            if index in visited:
                continue
            visited.add(index)
            for i in range(index+1,len(s)+1):
                if s[index:i] in word_set:
                    queue.append(i)
                    if i == len(s):
                        return True
        return False