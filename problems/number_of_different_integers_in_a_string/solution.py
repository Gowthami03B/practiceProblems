class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s=set()
        st=''
        for i in range(len(word)):
            if word[i].isnumeric():
                st+=word[i]
            elif st!='':
                s.add(int(st))
                st=''
        if st!='':
            s.add(int(st))
        return len(s)