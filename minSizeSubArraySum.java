package practice;

public class MinLenSubArraySum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MinLenSubArraySum m = new MinLenSubArraySum();
		int[] nums = {1,1,1};
		System.out.println(minSubArrayLen(7, nums));
	}
	
	 public static int minSubArrayLen(int target, int[] nums) {
		 int start = 0, sum = 0;
			int minLen = Integer.MAX_VALUE;
	        for(int i = 0; i< nums.length; i++){
	            sum += nums[i];
	            while(sum >= target){
	                minLen = Math.min(minLen, i + 1 - start);
	                sum -= nums[start];
	                start++;
	            }
	        }
	        return minLen != Integer.MAX_VALUE? minLen : 0;
	    }
}
