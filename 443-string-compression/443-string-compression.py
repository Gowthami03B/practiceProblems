class Solution:
    def compress1(self, chars: List[str]) -> int:
        i ,j = 0,1
        curr = chars[i]
        while i< len(chars) and j < len(chars):
            if chars[j] == curr: #current is next
                chars[j] = ""
                if j == len(chars) - 1: #for the last character in chars
                    if j-i < 9: #len < 9
                        chars[i+1] = str(j-i+1)#in the next ith position, we update count
                    else:
                        for d in str(j-i+1):#else for each digit in the count of char, we split it and update counts, say 123, a:1,2,3
                            chars[i+1] = d
                            i+= 1
            else:
                if j -i > 1 and j-i < 10:#if next char is not curr
                    chars[i+1] = str(j-i) #update count
                if j-i >= 10: #if >10, #else for each digit in the count of char, we split it and update counts, say 123, a:1,2,3
                    for d in str(j-i):
                        chars[i+1] = d
                        i+= 1
                i= j #once we find next group, set i to j
                curr = chars[i]#curr should next char group
            j += 1
        while("" in chars) :
            chars.remove("")
        print(chars)
        
    def compress(self, s: List[str]) -> int:
        i ,j = 0,1
        def replaceString(s,i,j):
            if j - i >= 1 and not s[j-1]:
                if j - i < 10:
                    s[j-1] = str(j-i)
                else:
                    char_count = str(j-i)
                    temp = j
                    for c in reversed(char_count):
                        s[temp-1] = c
                        temp -= 1
        while(i < len(s) and j < len(s)):
            if s[i] == s[j]:
                s[j] = ""
                j += 1
            else:
                replaceString(s,i,j)
                # if (j - i) < 10 and (j - i) > 1:
                #         s[j-1] = str(j-i)
                # elif j-i >= 10:
                #     char_count = str(j-i)
                #     temp = j
                #     for c in reversed(char_count):
                #         s[temp-1] = c
                #         temp -= 1
                i = j
                j += 1
        replaceString(s,i,j)
        while("" in s) :
            s.remove("")
        return len(s)
        
    