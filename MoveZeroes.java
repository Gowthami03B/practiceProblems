package practice;

import java.util.Arrays;

public class MoveZeroes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MoveZeroes m = new MoveZeroes();
		int[] val = { 0, 1, 0, 3, 12 };
		System.out.println(Arrays.toString(m.moveZeroes1(val)));
	}

	//Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
//	Note that you must do this in-place without making a copy of the array.
	
	public int[] moveZeroes1(int[] nums) {
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                nums[idx++] = nums[i];
            }
        }
        
        for (int i = idx; i < nums.length; i++) {
            nums[i] = 0;
        }
        return nums;
    }
}
