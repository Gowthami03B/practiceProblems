#O(n2)
def stringUniqueCharsBruteForce(s):
    if not s:
        return True
    for i in range(len(s)) :
        for j in range(i+1,len(s)):
            if(s[i] == s[j]):
                return False
    return True

#sorting - O(n log n)
def stringUniqueCharsSorting(s):
    if not s:
        return True
    s = sorted(s);
    for i in range(len(s) - 1) :
        if(s[i] == s[i+1]):
            return False
    return True

#O(N), space for res - O(1) (doesn't increase with size)
def stringUniqueCharsExtraSpace(s):
    if not s:
        return True
    res = [False for i in range(256)] #ASCII char set
    for c in s:
        if(res[ord(c) - ord('a')]):
            return False
        else:
            res[ord(c) - ord('a')] = True
    return True

#Time complexity O(N); Space - O(N) - set addition takes constant time, for n elements, O(N)
def stringUniqueCharsSets(s):
    if not s:
        return True
    setStr = set(s)
    if(len(s) == len(setStr)):
        return True
    else:
        return False

print(stringUniqueCharsSets("aaa"))
