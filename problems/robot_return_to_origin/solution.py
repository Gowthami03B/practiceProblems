class Solution:
    def judgeCircle(self, s: str) -> bool:
        x = 0
        y = 0
        for c in s:
            if c == 'L':
                y -= 1
            elif c == 'R':
                y += 1
            elif c == 'D':
                x -= 1
            elif c == 'U':
                x += 1
        return True if x == 0 and y == 0 else False