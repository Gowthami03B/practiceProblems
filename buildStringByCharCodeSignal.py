"""
You are given an array of strings arr. Your task is to construct a string from the words in arr, starting with the 0th character from each word (in the order they appear in arr), followed by the 1st character, then the 2nd character, etc. If one of the words doesn't have an ith character, skip that word.

Return the resulting string.

Example

For arr = ["Daisy", "Rose", "Hyacinth", "Poppy"], the output should be solution(arr) = "DRHPaoyoisapsecpyiynth".

First, we append all 0th characters and obtain string "DRHP";
Then we append all 1st characters and obtain string "DRHPaoyo";
Then we append all 2nd characters and obtain string "DRHPaoyoisap";
Then we append all 3rd characters and obtain string "DRHPaoyoisapsecp";
Then we append all 4th characters and obtain string "DRHPaoyoisapsecpyiy";
Finally, only letters in the arr[2] are left, so we append the rest characters and get "DRHPaoyoisapsecpyiynth"

"""
def solution(arr):
    if len(arr) == 1:
        return arr[0]
    output = ""
    length = len(min(arr, key = len))
    max_len = len(max(arr, key = len))
    # print(max_len)
    for s in zip(*arr):
        for c in s:
            output += c
        
    # print(output, length)
    while length < max_len:
        for s in arr:
            if len(s) > length:
                output += s[length]
        length += 1
    return output
arr = ["Daisy", "Rose", "Hyacinth", "Poppy"]
arr1=["We","Ore","a","sdyeir"]
#DRHPaoyoisapsecpyiynth
print(solution(arr1))
