class Solution {
    public int maximumDifference(int[] nums) {
        int maxDiff = 0;
        for(int i =0; i <nums.length; i++){
            for(int j = i+1; j < nums.length; j++){
                if(nums[i] < nums[j])
                    maxDiff = Math.max(maxDiff, nums[j] - nums[i]);
            }
        }
        if (maxDiff > 0)
            return maxDiff;    
        else return -1;
    }
}