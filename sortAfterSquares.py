"""

you will be given an array of integers in ascending order .You have to print the square of the elements in ascending order.


input: [1, 2, 4]

output: [1, 4, 16]

[-2, -1, 5, 10, 12]
[4,1,25,100,144]
1 4 25 100 144

[-2,-1,0,1,2]
[4,1,0,1,4]
[0,1,4,4]

neg - abs, sort, output
pos - nothing
pos, neg - then for neg part we need to do something
      l        
[-5, -2, 1, 3, 7]
            r
[25,4,1,9,49]
7 5 3 2 1
1 2 3 5 7
 
"""
#O(n log n), o(1)
def square(nums):
  res = [x*x for x in nums]
  res.sort()
  return res

#O(N), o(N)
def squareTwopointers(nums):
  i,j, index = 0, len(nums) - 1,  len(nums) - 1
  res = [0] * len(nums) #populating this list of correct size is
  while(index >= 0):
    if abs(nums[i]) >= abs(nums[j]):
      res[index] = nums[i] * nums[i]
      i += 1
    else:
      res[index] = nums[j] * nums[j]
      j -= 1
    index -= 1
  return res

def mergeSort(nums):
  k = 0
  n = len(nums)
  for k in range(n):
    if nums[k] > 0: #find the end of negative elements
      break
  print(k)
  i,j = k-1, k #loop through negative elements from end to start as first negative number would be smallest
  idx = 0
  temp = [0] * n
  while(i >=0 and j <n):
    if nums[i]*nums[i] >= nums[j]*nums[j]:
      temp[idx] = nums[j]*nums[j]
      j += 1
    else:
      temp[idx] = nums[i]*nums[i]
      i -= 1
    idx += 1
  print(temp,i,j) #after above loop - [1, 25, 100, 144, 0]
#only the largest numbers would be left out on each side
#update remaining elements starting with negative numbers
  while(i >= 0):
    temp[idx] = nums[i]*nums[i]
    i -= 1
    idx += 1
#update remaining elements 
  while(j < n):
    temp[idx] = nums[j]*nums[j]
    j += 1
    idx += 1
  
  return temp

nums = [-20, -1, 5, 10, 12, 26]
print(mergeSort(nums))
