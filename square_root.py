# Given an integer, find its square root without using built-in square root function. Only return the integer part (truncate the decimals)
def square_root(n: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    low , high = 1, n//2
    ans = 1
    while low <= high:
        mid = (low+high)//2
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans
         

if __name__ == '__main__':
    n = int(input())
    res = square_root(n)
    print(res)
