class Solution {
    public int countBinarySubstrings(String s) {
            int count = 0;
            int consecutiveCount = 1;
            int lastConsecutiveCount = 0;
            char[] c = s.toCharArray();
            for (int i = 1; i < c.length; i++)
            {
                if (c[i] != c[i - 1])
                {
                    lastConsecutiveCount = consecutiveCount;
                    consecutiveCount = 1;
                    count++;
                }
                else
                {
                    consecutiveCount++;
                    if (consecutiveCount <= lastConsecutiveCount) count++;
                }
            }

            return count;
        }
}