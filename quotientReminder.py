"""
Given a numerator and a divisor of unsigned ints, print out the quotient and the remainder. Caveats: cannot use divide, cannot use mod
Example: 31/5, if num = 31, div = 5, print "q: 6, r: 1"

5+5+5+5*5*5*5 = 31 - O(quotient)

31/2 - 15, 31 - (5+5+5)*2

loop from div, num - if div * div + 1 < num - diff (rem), > num, return rem

div * quo + x = num => num - (div * q) = x
5   * 0  + x = 31 - 5 = 1
9/2
left - 0, right - 9
mid - 5
9 - 2*5 = -1 < 0;
right = mid
mid = 2
9 - 2*2 = 5
left = mid+1 - 3..5
9 - 6 =3
left = 4..5
9-8 =1 

1/0
"""
# we need to think about 2 main key things here - num = div*quo + rem
# i.e rem = (num - div*quo), by varying quotient we can find remainder
#also if divisor is x, then remainder is always between 0 and x-1

#O(Quotient), O(1)
def bruteforce(num, div):
    if div == 0: #handle divisor 0
        return []
    if div == 1: #handle divisor 1
        return[num,0]
    for i in range(1, num//2 + 1): #but loop only runs until we find the quotient
        rem = num - (div*i)
        if rem <= (div - 1):
            return [i,rem]
  
def binarySearch(num, div):
    if div == 0:
        return []
    if div == 1:
        return[num,0]
    start , end = 1, num - 1
    while(start <= end):
      mid = (start + end)//2
      rem = num - (div*mid)
      if rem  > div: #need to increase quotient
        start = mid + 1
      elif rem < 0: #need to decrease quotient
        end = mid - 1
      else:
        if rem == div:#perfectly divisible 25/5, at quo=4, rem ==5 and equal to divisor
          mid += 1
          rem = 0
        return [mid, rem]
