class Solution:
    #horizontal scanning - worst case is n same strings with length m; we need to do n*m character comparisons of all chars in all strings 
    #if the smallest string is at the end of the array, we keep looping thru all other strings unnecessarily same comparisons as above
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if not strs or len(strs) == 0:
            return ""
        prefix = strs[0]#consider 1st string as prefix
        
        for s in strs[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]#reduce prefix size by 1
                if not prefix:#if prefix becomes empty, no common return
                    return ""
        return prefix
    
    #vertical scanning- worst case is n same strings with length m; we need to do n*m character comparisons of all chars in all strings 
    #in best case, if the smallest string is at the end of the array, we need to do only n*minLength char comparisons as the zips stops at the smallest string
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #our program doesn't keep running beyond the smallest string
        if not strs or len(strs) == 0:
            return ""
        result = []
        #["flower","flow","flight"]
        for s in zip(*strs):#unzips strings into iterable sequences as tuples
        #(f,f,f),(l,l,l)(o,o,i)(w,w,g) and stops because it constructs until shortest string
            if len(set(s)) != 1:#if all the chars are not same break
                break
            result.append(s[0])#else append to result, we can also do result += s[0], but this way we create many substrings
        return "".join(result)
            