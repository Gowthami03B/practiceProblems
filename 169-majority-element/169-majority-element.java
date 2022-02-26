class Solution {
    public int majorityElement(int[] nums) {
        int maxTimes = nums.length/2;
        Map<Integer, Integer> map = new HashMap<>();
        for(int n : nums){
             map.put(n, map.getOrDefault(n,0)+1);
        }
        for(int key : map.keySet()){
            if(map.get(key) > maxTimes){
                return key;
            }
        }
       return -1; 
    }
}