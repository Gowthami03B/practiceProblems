class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        line = []
        word_count = 0
        char_count = 0
        res = []
        for word in words:
            length = char_count+1+len(word)
            if length > maxWidth:
                space_left = maxWidth - char_count
                if word_count == 1:
                    string = line[0]+" "*(maxWidth-len(line[0]))
                    res.append(string)
                    line = [word]
                    char_count = len(word)
                else:
                    q, r = divmod(space_left, word_count-1)
                    front = (" "*(q+2)).join(line[:r+1])
                    end = (" "*(q+1)).join(line[r+1:])
                    string = front+" "*(q+1)+end
                    if string:
                        res.append(string)
                    line = [word]
                    word_count = 1
                    char_count = len(word)
            else:
                if line:
                    char_count += len(word)+1
                else:
                    char_count += len(word)
                line.append(word)
                word_count += 1
        if line:
            line = " ".join(line)
            line += " "*(maxWidth-len(line))
            res.append(line)
        return res