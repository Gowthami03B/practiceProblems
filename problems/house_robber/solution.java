class Solution {
    public int rob(int[] nums) {
    //example of how bad someone can analyze the problem
    //    int even_cnt = 0, odd_cnt = 0;
    //    for(int i=0; i < nums.length; i++){
    //        if(i%2 == 0){
    //            even_cnt += nums[i];
    //        }else{
    //            odd_cnt += nums[i];
    //        }    
    //    }   
    //    return Math.max(even_cnt, odd_cnt); 
    // }
    if(nums.length == 0 || nums == null)
        return 0;
    if(nums.length == 1)
        return nums[0];
    if(nums.length == 2)
        return Math.max(nums[0], nums[1]);
    int[] dp = new int[nums.length];
    dp[0] = nums[0];
    dp[1] = Math.max(nums[0], nums[1]);
    //using only 2 variables
    int rob1 = nums[0], rob2 = Math.max(nums[0], nums[1]);
    for(int i = 2; i < nums.length; i++){
        dp[i] = Math.max(nums[i] + dp[i-2], dp[i-1]);
        // rob1 = rob2;
        // rob2 = maxProfit;
    }
    return dp[nums.length - 1];
}
}