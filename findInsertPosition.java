// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You must write an algorithm with O(log n) runtime complexity.
package practice;

public class findInsertPos {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int val[] = { 1};
		findInsertPos c = new findInsertPos();
		System.out.println(c.searchInsertRegular(val, 2));

	}
	
//	Time Complexity: O(log N)
//	Space: O(1)
	public int searchInsertOptimal(int[] nums, int target) {
		int start = 0;
		int end = nums.length - 1;
		while(start <= end) {
			int mid = (start + end)/2;
			if(target == nums[mid]){
				return mid;
			}
			else if(target > nums[mid]) {
				start = mid + 1;
			}else {
				end = mid - 1;
			}
		}
		return end + 1;
	}
	
//	Time Complexity: O(N)
//	Space: O(1)
	public int searchInsertRegular(int[] nums, int target) {
		for(int i = 0 ; i < nums.length; i++) {
			if(target == nums[i])
				return i;
		}
		return nums.length;
	}

}
