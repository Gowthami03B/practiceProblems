class Solution:
    def isPalindrome(self, x: int) -> bool:#O(log10(n)), as divide by 10 and reduce the number of steps
        if x < 0:
            return False
        temp = x
        reverse = 0
        count = 0
        while(x):
            reminder = x % 10
            x = x//10
            reverse = reverse* 10 + reminder
            count += 1
        print(count,temp)#10 1111221111
        return reverse == temp

    def isPalindrome1(self, x: int) -> bool:#Time complexity : O(log⁡10(n/2)) == O(log10(n)). We divided the input by 10 for every iteration and reduced the number of steps, so the time complexity is O(log⁡10(n))
        temp = x
        if x < 0 or (x%10 == 0 and x!=0):
            return False

        reverse = 0
        count = 0
        while(x > reverse):#to go through half of the number
            reminder = x % 10
            x = x//10
            reverse = reverse* 10 + reminder
            count += 1
        print(count,temp)#5 1111221111
        print(x,reverse)
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123,
        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == reverse or x == reverse//10

    