"""
// The number 1112221111 can be read out as "one, one, one, two, ..." etc: saying each digit from left to right. However, we could be more efficient by grouping like digits. In this case: "three ones, three twos, four ones." This leads to the encoding 313241 (read it out loud!).

// Write a program to encode integers in this way.

// Note: consider the speed of your program: try to avoid expensive string operations.
// 111222. -> 3132

// 3, 1, 3, 2 -->. 3132

O(1) space
Any ideas?
"""
def encodeInteger(number):
    start = 0
    result = []
    for i in range(1,len(number)):
        if number[i] == number[i-1]:
            continue
        else:
            result.append(str(i-start))
            start = i
            result.append(number[i-1])
    
    if i - start + 1 > 0:
        result.append(str(i-start+1))
        result.append(number[i-1])
    print(result)
    return "".join(result)

print(encodeInteger("12221111"))
