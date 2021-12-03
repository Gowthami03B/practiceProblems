package practice;

public class sortedRotatedArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int val[] = {4,5,6,7,0,1,2};
		sortedRotatedArray c = new sortedRotatedArray();
		System.out.println(c.sortedRotatedArrayTar(val, 0));

	}
	
//	Time Complexity: O(log N)
	public int sortedRotatedArrayTar(int[] nums, int target) {
		if (nums == null || nums.length == 0) return -1;
		int left = 0;
		int right = nums.length - 1;
		//finding the smallest element in the array
		while(left < right) {
			int mid = (left + right)/2;
			if(nums[mid] > nums[right]) { //if mid > right most element which is not the case for a sorted array, we can narrow our search to the left hand side
				left = mid + 1;
			}else {
				right = mid;//else continue on the right side
			}
		}
		int start = left;
		left = 0;
		right = nums.length - 1;
		if(target >= nums[start] && target <= nums[right]) {
			left =  start;
		}else {
			right = start; //left is already assigned to 0
		}
		while(left <= right) {
			int mid = (left + right)/2;
			if(nums[mid] == target) {
				return mid;
			}else if(nums[mid] < target) {
				left = mid + 1;
			}else {
				right = mid - 1;
			}
		}
		return -1;
	}

}
