class Solution {
    public boolean isMajorityElement(int[] nums, int target) {
        int count = 0; int ele = 0;
        for(int n : nums){
            if(n == target)
                count++;
        }
        if(count > (nums.length/2))
            return true;
        return false;
    }
}