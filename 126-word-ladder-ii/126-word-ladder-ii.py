class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList)
        if endWord not in wordList:#return []
            return []
        # BFS visit
        curr_level = {beginWord}#start from beginWord
        parents = collections.defaultdict(list)
        while curr_level:
            wordList -= curr_level
            next_level = set()
            for word in curr_level:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]#construct the comb
                        if new_word in wordList:
                            next_level.add(new_word)#add to next level
                            parents[new_word].append(word)
            if endWord in next_level:
                break
            curr_level = next_level
        # DFS reconstruction
        res = []
        def dfs(word, path):
            if word == beginWord:
                path.append(word)
                res.append(path[::-1])
            else:
                for p_word in parents[word]:
                    dfs(p_word, path + [word])
        dfs(endWord, [])#dfs from endWord
        return res
        