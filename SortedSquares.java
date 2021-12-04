package practice;

import java.util.Arrays;

public class SortedSquares {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int val[] = {-4,-1,0,3,10};
		SortedSquares c = new SortedSquares();
		System.out.println(Arrays.toString(c.sortedSquares(val)));
	}
	
	//Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
	//2-pointer approach
	public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;
        int res[] = new int[n];
        for(int i = n -1; i >= 0 ; i-- ){
            if(Math.abs(nums[left]) > Math.abs(nums[right])){
                res[i] = nums[left] * nums[left];
                left++;
            }else{
                res[i] = nums[right] * nums[right];
                right--;
            }
        }
        return res;
    }
}
