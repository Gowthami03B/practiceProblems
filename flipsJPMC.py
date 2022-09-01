"""
Given a string S, the task is to find minimum flips required to convert an initial binary string consisting of only zeroes to S where every flip of a character flips all succeeding characters as well. 
Examples: 
 

Input: S = “01011” 
Output: 3 
Explanation: 
Initial String – “00000” 
Flip the 2nd bit – “01111” 
Flip the 3rd bit – “01000” 
Flip the 4th bit – “01011” 
Total Flips = 3
"""
def flips(target):
    curr = '1'#if the curr is 1, then we are making a change, and all values become 1
    #after which we change curr to 0, if next bit is 0, we need to flip again, hence count becomes +1 and so on
    count = 0
     
    for i in range(len(target)):
         
        # If curr occurs in the final string
        if (target[i] == curr):
            count += 1
             
            # Switch curr to '0' if '1'
            # or vice-versa
            curr = chr(48 + (ord(curr) + 1) % 2)#ord(0) = 48, ord(1)=49; ord(curr)+1)%2 gives 0 for 0 and 1 for 1
     
    return count

print(flips("00001"))
