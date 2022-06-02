class Solution:
    def compress(self, chars: List[str]) -> int:
        i ,j = 0,1
        curr = chars[i]
        while i< len(chars) and j < len(chars):
            if chars[j] == curr:
                chars[j] = ""
                if j == len(chars) - 1:
                    if j-i < 9:
                        chars[i+1] = str(j-i+1)
                    else:
                        for d in str(j-i+1):
                            chars[i+1] = d
                            i+= 1
            else:
                if j -i > 1 and j-i < 10:
                    chars[i+1] = str(j-i)
                if j-i >= 10:
                    for d in str(j-i):
                        chars[i+1] = d
                        i+= 1
                i= j
                curr = chars[i]
            j += 1
        while("" in chars) :
            chars.remove("")
        print(chars)