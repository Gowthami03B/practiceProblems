package practice;

public class MaxSumSubArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MaxSumSubArray m = new MaxSumSubArray();
		int[] nums = {1};
		System.out.println(m.minSubArrayLen(nums));
	}
	//dynamic programming
	//kadanes algorithm
	//The simple idea of Kadane’s algorithm is to look for all positive contiguous segments of the array (sum is used for this). 
//	And keep track of maximum sum contiguous segment among all positive segments (max_so_far is used for this). 
//	Each time we get a positive-sum compare it with max_so_far and update max_so_far if it is greater than sum
	//The maximum subarray problem is a task to find the series of contiguous elements with the maximum sum in any given array.
	//below solution doesn't handle case where all array numbers are negative
	
	//extension to this problem is to find the start and end indices
	 public int minSubArrayLen(int[] nums) {
		 int max_so_far = Integer.MIN_VALUE, sum = 0, s = 0, start = 0, end = 0;
	        for(int i = 0; i< nums.length; i++){
	        	sum += nums[i];
	        	if(nums.length == 1)
	        		return nums[i];
	            if(sum < 0) {
	            	sum = 0;
	            	s = i + 1;
	            }
	            if(max_so_far < sum) {
	            	max_so_far = sum;
	            	start = s;
	            	end = i;
	            }
	        }
	        System.out.println(start);
	        System.out.println(end);
	        return max_so_far;
	    }
	 
	 public int whenAllNumsAreNeg(int[] nums) {
		 int max_so_far = nums[0], sum = nums[0];
	        for(int i = 1; i< nums.length; i++){
	        	sum = Math.max(nums[i], sum + nums[i]);
	        	max_so_far = Math.max(max_so_far, sum);
	        }
	        return max_so_far;
	    }
}
