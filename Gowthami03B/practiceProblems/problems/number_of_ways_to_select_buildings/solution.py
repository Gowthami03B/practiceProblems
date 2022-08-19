class Solution:
    def numberOfWays(self, s: str) -> int:
        """
        For "1", we want "010"
For "0", we want "101"
Thus, all we need to do is to count how many 0s and 1s are before/after 1 and 0
        """
        ans=0
        n=len(s)
        left=[0]*n
        right=[0]*n
        zeros,ones=0,0
        for i in range(n):
            if s[i]=="0": 
                zeros+=1
                left[i]=ones#no of 1's before this 0
            else: 
                ones+=1
                left[i]=zeros#no of 0's before this 1
        # print(left,right)
        #prefix comb [0, 0, 2, 2, 2, 3] [0, 0, 0, 0, 0, 0]
        #counting no of 1's or 0's before so we know how many combinations that can be made
        #in reverse right -[3,3,1,1,1,0] suffix comb
        zeros,ones=0,0
        for i in range(n-1,-1,-1):
            if s[i]=="0": 
                zeros+=1
                right[i]=ones#no of 1's after this 0
            else: 
                ones+=1
                right[i]=zeros#no of 0's after this 1
            ans+=left[i]*right[i]#product of both is the ans
        return ans